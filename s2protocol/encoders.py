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

class IncompleteError(Exception):
    pass


class BitPackedBuffer:
    def __init__(self, output, endian = 'big'):
        self._output = output
        self._next = 0
        self._used_bits = 0
        self._bigendian = (endian == 'big')

    def __str__(self):
        return 'buffer(%d)' % (self._used_bits,)

    def used_bits(self):
        return self._used_bits

    def byte_align(self):
        if (self._used_bits & 7) != 0:
            self._output.write(chr(self._next))
            self._next = 0
            self._used_bits = (self._used_bits + 7) & ~7

    def write_aligned_bytes(self, data):
        assert isinstance(data, str)
        self.byte_align()
        self._used_bits += len(data) * 8
        self._output.write(data)

    def write_bits(self, value, bits):
        writtenbits = 0
        while writtenbits != bits:
            copybits = min(bits - writtenbits, 8 - ((self._used_bits) & 7))
            if self._bigendian:
                copy = value >> (bits - writtenbits - copybits)
            else:
                copy = value >> writtenbits
            self._next |= (copy & ((1 << copybits) - 1)) << (self._used_bits & 7)
            writtenbits += copybits
            self._used_bits += copybits
            if (self._used_bits & 7) == 0:
                self._output.write(chr(self._next))
                self._next = 0
                assert self._output.tell() == self._used_bits / 8

    def write_unaligned_bytes(self, data):
        assert isinstance(data, str)
        for c in data:
            self.write_bits(byte_to_int(c), 8)

class BitPackedEncoder:
    def __init__(self, output, typeinfos):
        self._buffer = BitPackedBuffer(output)
        self._typeinfos = typeinfos

    def __str__(self):
        return self._buffer.__str__()

    def instance(self, value, typeid):
        if typeid >= len(self._typeinfos):
            raise CorruptedError(self)
        typeinfo = self._typeinfos[typeid]
        return getattr(self, typeinfo[0])(value, *typeinfo[1])

    def byte_align(self):
        self._buffer.byte_align()

    def used_bits(self):
        return self._buffer.used_bits()

    def _array(self, value, bounds, typeid):
        assert isinstance(value, list)
        self._int(len(value), bounds)
        for element in value:
            self.instance(element, typeid)

    def _bitarray(self, value, bounds):
        assert isinstance(value, tuple)
        self._int(value[0], bounds)
        self._buffer.write_bits(value[1], value[0])

    def _blob(self, value, bounds):
        assert isinstance(value, str)
        self._int(value, bounds)
        self._buffer.write_aligned_bytes(value)

    def _bool(self, value):
        self._buffer.write_bits(1 if (value != False) else 0, 1)

    def _choice(self, value, bounds, fields):
        #assert isinstance(value, dict)
        assert len(value) == 1
        for tag, field in fields.items():
            if field[0] in value:
                self._int(tag, bounds)
                self.instance(value[field[0]], field[1])
                break
        else:
            raise IncompleteError(self) # unknown choice field name

    def _fourcc(self, value):
        assert isinstance(value, str)
        assert len(value) == 4
        self._buffer.write_aligned_bytes(value)

    def _int(self, value, bounds):
        assert value >= bounds[0]
        assert value < bounds[0] + (1 << bounds[1])
        self._buffer.write_bits(value - bounds[0], bounds[1])

    def _null(self, value):
        pass

    def _optional(self, value, typeid):
        self._buffer.write_bits(1 if (value is not None) else 0, 1)
        if value is not None:
            self.instance(value, typeid)

    def _real32(self):
        assert isinstance(value, float)
        self._buffer.write_unaligned_bytes(struct.pack('>f', value))

    def _real64(self, value):
        assert isinstance(value, float)
        self._buffer.write_unaligned_bytes(struct.pack('>d', value))

    def _struct(self, value, fields):
        #assert isinstance(value, dict)
        # encode each field
        for field_name, field_type, _ in fields:
            if field_name == '__parent':
                # if there is a parent its fields are in the same value dict
                self.instance(value, field_type)
            elif field_name in value:
                self.instance(value[field_name], field_type)
            else:
                raise IncompleteError(self) # missing field_name

class VersionedEncoder:
    def __init__(self, output, typeinfos):
        self._buffer = BitPackedBuffer(output)
        self._typeinfos = typeinfos

    def __str__(self):
        return self._buffer.__str__()

    def instance(self, value, typeid):
        if typeid >= len(self._typeinfos):
            raise CorruptedError(self)
        typeinfo = self._typeinfos[typeid]
        return getattr(self, typeinfo[0])(value, *typeinfo[1])

    def byte_align(self):
        self._buffer.byte_align()

    def used_bits(self):
        return self._buffer.used_bits()

    def _write_skip(self, skip):
        self._buffer.write_bits(skip, 8)

    def _vint(self, value, bounds=None):
        assert bounds is None or value >= bounds[0]
        assert bounds is None or value < bounds[0] + (1 << bounds[1])
        negative = (value < 0)
        if negative:
            value = -value
        b = ((value & 0x3f) << 1) | (1 if negative else 0)
        value >>= 6
        self._buffer.write_bits(b | (0x80 if (value != 0) else 0x00), 8)
        while value != 0:
            b = value & 0x7f
            value >>= 7
            self._buffer.write_bits(b | (0x80 if (value != 0) else 0x00), 8)

    def _array(self, value, bounds, typeid):
        assert isinstance(value, list)
        self._write_skip(0)
        self._vint(len(value), bounds)
        for element in value:
            self.instance(element, typeid)

    def _bitarray(self, value, bounds):
        assert isinstance(value, tuple)
        self._write_skip(1)
        self._vint(value[0], bounds)
        self._buffer.write_aligned_bytes(value[1])

    def _blob(self, value, bounds):
        assert isinstance(value, str)
        self._write_skip(2)
        self._vint(len(value), bounds)
        self._buffer.write_aligned_bytes(value)

    def _bool(self, value):
        self._write_skip(6)
        self._buffer.write_bits(1 if (value != False) else 0, 8)

    def _choice(self, value, bounds, fields):
        #assert isinstance(value, dict)
        assert len(value) == 1
        self._write_skip(3)
        for tag, field in fields.items():
            if field[0] in value:
                self._vint(tag)
                self.instance(value[field[0]], field[1])
                break
        else:
            raise IncompleteError(self) # unknown choice field name

    def _fourcc(self, value):
        assert isinstance(value, str)
        assert len(value) == 4
        self._write_skip(7)
        self._buffer.write_aligned_bytes(value)

    def _int(self, value, bounds):
        self._write_skip(9)
        self._vint(value, bounds)

    def _null(self):
        pass

    def _optional(self, value, typeid):
        self._write_skip(4)
        self._buffer.write_bits(1 if (value is not None) else 0, 8)
        if value is not None:
            self.instance(value, typeid)

    def _real32(self, value):
        assert isinstance(value, float)
        self._write_skip(7)
        self._buffer.write_aligned_bytes(struct.pack('>f', value))

    def _real64(self, value):
        assert isinstance(value, float)
        self._write_skip(8)
        self._buffer.write_aligned_bytes(struct.pack('>d', value))

    def _struct(self, value, fields):
        #assert isinstance(value, dict)
        self._write_skip(5)
        # encode number of fields
        field_count = 0
        for field_name, _, _ in fields:
            if field_name == '__parent' or field_name in value:
                field_count += 1
        self._vint(field_count)
        # encode each field
        for field_name, field_type, field_tag in fields:
            if field_name == '__parent':
                # if there is a parent its fields are in the same value dict
                self._vint(field_tag)
                self.instance(value, field_type)
            elif field_name in value:
                self._vint(field_tag)
                self.instance(value[field_name], field_type)

