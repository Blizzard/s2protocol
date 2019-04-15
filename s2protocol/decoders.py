# Copyright (c) 2013-2017 Blizzard Entertainment
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import struct

from s2protocol.compat import byte_to_int


class TruncatedError(Exception):
    pass


class CorruptedError(Exception):
    pass


class BitPackedBuffer:
    def __init__(self, contents, endian='big'):
        self._data = contents or []
        self._used = 0
        self._next = None
        self._nextbits = 0
        self._bigendian = (endian == 'big')

    def __str__(self):
        s = '{:02x}'.format(byte_to_int(self._data[self._used])) \
            if self._used < len(self._data) else '--'
        return 'buffer({0:02x}/{1:d},[{2:d}]={3:s})'.format(
            self._nextbits and self._next or 0,
            self._nextbits,
            self._used,
            s
        )

    def done(self):
        return self._nextbits == 0 and self._used >= len(self._data)

    def used_bits(self):
        return self._used * 8 - self._nextbits

    def byte_align(self):
        self._nextbits = 0

    def read_aligned_bytes(self, bytes):
        self.byte_align()
        data = self._data[self._used:self._used + bytes]
        self._used += bytes
        if len(data) != bytes:
            raise TruncatedError(self)
        return data

    def read_bits(self, bits):
        result = 0
        resultbits = 0
        while resultbits != bits:
            if self._nextbits == 0:
                if self.done():
                    raise TruncatedError(self)
                self._next = byte_to_int(self._data[self._used])
                self._used += 1
                self._nextbits = 8
            copybits = min(bits - resultbits, self._nextbits)
            copy = (self._next & ((1 << copybits) - 1))
            if self._bigendian:
                result |= copy << (bits - resultbits - copybits)
            else:
                result |= copy << resultbits
            self._next >>= copybits
            self._nextbits -= copybits
            resultbits += copybits
        return result

    def read_unaligned_bytes(self, bytes):
        return ''.join([chr(self.read_bits(8)) for i in range(bytes)])


class BitPackedDecoder:
    def __init__(self, contents, typeinfos):
        self._buffer = BitPackedBuffer(contents)
        self._typeinfos = typeinfos

    def __str__(self):
        return self._buffer.__str__()

    def instance(self, typeid):
        if typeid >= len(self._typeinfos):
            raise CorruptedError(self)
        typeinfo = self._typeinfos[typeid]
        #print ' -- instance ', typeid, typeinfo
        return getattr(self, typeinfo[0])(*typeinfo[1])

    def byte_align(self):
        self._buffer.byte_align()

    def done(self):
        return self._buffer.done()

    def used_bits(self):
        return self._buffer.used_bits()

    def _array(self, bounds, typeid):
        length = self._int(bounds)
        return [self.instance(typeid) for i in range(length)]

    def _bitarray(self, bounds):
        length = self._int(bounds)
        return (length, self._buffer.read_bits(length))

    def _blob(self, bounds):
        length = self._int(bounds)
        result = self._buffer.read_aligned_bytes(length)
        return result

    def _bool(self):
        return self._int((0, 1)) != 0

    def _choice(self, bounds, fields):
        tag = self._int(bounds)
        if tag not in fields:
            raise CorruptedError(self)
        field = fields[tag]
        return {field[0]: self.instance(field[1])}

    def _fourcc(self):
        return self._buffer.read_unaligned_bytes(4)

    def _int(self, bounds):
        return bounds[0] + self._buffer.read_bits(bounds[1])

    def _null(self):
        return None

    def _optional(self, typeid):
        exists = self._bool()
        return self.instance(typeid) if exists else None

    def _real32(self):
        return struct.unpack('>f', self._buffer.read_unaligned_bytes(4))

    def _real64(self):
        return struct.unpack('>d', self._buffer.read_unaligned_bytes(8))

    def _struct(self, fields):
        result = {}
        for field in fields:
            if field[0] == '__parent':
                parent = self.instance(field[1])
                if isinstance(parent, dict):
                    result.update(parent)
                elif len(fields) == 1:
                    result = parent
                else:
                    result[field[0]] = parent
            else:
                result[field[0]] = self.instance(field[1])
        return result


class VersionedDecoder:
    def __init__(self, contents, typeinfos):
        self._buffer = BitPackedBuffer(contents)
        self._typeinfos = typeinfos

    def __str__(self):
        return self._buffer.__str__()

    def instance(self, typeid):
        if typeid >= len(self._typeinfos):
            raise CorruptedError(self)
        typeinfo = self._typeinfos[typeid]
        return getattr(self, typeinfo[0])(*typeinfo[1])

    def byte_align(self):
        self._buffer.byte_align()

    def done(self):
        return self._buffer.done()

    def used_bits(self):
        return self._buffer.used_bits()

    def _expect_skip(self, expected):
        if self._buffer.read_bits(8) != expected:
            raise CorruptedError(self)

    def _vint(self):
        b = self._buffer.read_bits(8)
        negative = b & 1
        result = (b >> 1) & 0x3f
        bits = 6
        while (b & 0x80) != 0:
            b = self._buffer.read_bits(8)
            result |= (b & 0x7f) << bits
            bits += 7
        return -result if negative else result

    def _array(self, bounds, typeid):
        self._expect_skip(0)
        length = self._vint()
        return [self.instance(typeid) for i in range(length)]

    def _bitarray(self, bounds):
        self._expect_skip(1)
        length = self._vint()
        return (length, self._buffer.read_aligned_bytes((length + 7) / 8))

    def _blob(self, bounds):
        self._expect_skip(2)
        length = self._vint()
        return self._buffer.read_aligned_bytes(length)

    def _bool(self):
        self._expect_skip(6)
        return self._buffer.read_bits(8) != 0

    def _choice(self, bounds, fields):
        self._expect_skip(3)
        tag = self._vint()
        if tag not in fields:
            self._skip_instance()
            return {}
        field = fields[tag]
        return {field[0]: self.instance(field[1])}

    def _fourcc(self):
        self._expect_skip(7)
        return self._buffer.read_aligned_bytes(4)

    def _int(self, bounds):
        self._expect_skip(9)
        return self._vint()

    def _null(self):
        return None

    def _optional(self, typeid):
        self._expect_skip(4)
        exists = self._buffer.read_bits(8) != 0
        return self.instance(typeid) if exists else None

    def _real32(self):
        self._expect_skip(7)
        return struct.unpack('>f', self._buffer.read_aligned_bytes(4))

    def _real64(self):
        self._expect_skip(8)
        return struct.unpack('>d', self._buffer.read_aligned_bytes(8))

    def _struct(self, fields):
        self._expect_skip(5)
        result = {}
        length = self._vint()
        for i in range(length):
            tag = self._vint()
            field = next((f for f in fields if f[2] == tag), None)
            if field:
                if field[0] == '__parent':
                    parent = self.instance(field[1])
                    if isinstance(parent, dict):
                        result.update(parent)
                    elif len(fields) == 1:
                        result = parent
                    else:
                        result[field[0]] = parent
                else:
                    result[field[0]] = self.instance(field[1])
            else:
                self._skip_instance()
        return result

    def _skip_instance(self):
        skip = self._buffer.read_bits(8)
        if skip == 0:  # array
            length = self._vint()
            for i in range(length):
                self._skip_instance()
        elif skip == 1:  # bitblob
            length = self._vint()
            self._buffer.read_aligned_bytes((length + 7) / 8)
        elif skip == 2:  # blob
            length = self._vint()
            self._buffer.read_aligned_bytes(length)
        elif skip == 3:  # choice
            tag = self._vint()
            self._skip_instance()
        elif skip == 4:  # optional
            exists = self._buffer.read_bits(8) != 0
            if exists:
                self._skip_instance()
        elif skip == 5:  # struct
            length = self._vint()
            for i in range(length):
                tag = self._vint()
                self._skip_instance()
        elif skip == 6:  # u8
            self._buffer.read_aligned_bytes(1)
        elif skip == 7:  # u32
            self._buffer.read_aligned_bytes(4)
        elif skip == 8:  # u64
            self._buffer.read_aligned_bytes(8)
        elif skip == 9:  # vint
            self._vint()
