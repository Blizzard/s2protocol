import sys

__all__ = 'byte_to_int',


def byte_to_int(x):
    if sys.version_info.major == 3 and isinstance(x, bytes):
        return x
    else:
        return ord(x)
