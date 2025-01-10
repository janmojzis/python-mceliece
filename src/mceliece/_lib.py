from ctypes.util import find_library as _find_library
from ctypes import CDLL as _CDLL

_libname = _find_library('mceliece')
if _libname is None:
    raise FileNotFoundError("unable to locate library 'mceliece'")
_lib = _CDLL(_libname)


def _check_input(x, xlen, name):
    if not isinstance(x, bytes):
        raise TypeError(f'{name} must be bytes')
    if xlen != -1 and xlen != len(x):
        raise ValueError(f'{name} length must have exactly {xlen} bytes')
