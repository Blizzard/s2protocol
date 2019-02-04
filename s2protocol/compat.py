from six import PY3, binary_type

__all__ = 'byte_to_int',


def byte_to_int(x):
    if PY3 and isinstance(x, binary_type):
        return x
    else:
        return ord(x)
