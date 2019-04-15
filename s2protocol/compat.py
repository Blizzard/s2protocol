import sys
import io

__all__ = 'PY3', 'byte_to_int', 'get_stream'
PY3 = sys.version_info.major == 3


def byte_to_int(x):
    if PY3 and isinstance(x, (bytes, int)):
        return x
    else:
        return ord(x)


def get_stream():
    if PY3:
        cls = io.StringIO
    else:
        cls = io.BytesIO
    return cls()
