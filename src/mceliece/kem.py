from typing import Tuple as _Tuple
import ctypes as _ct
from ._lib import _lib, _check_input


class _KEM:
    def __init__(self) -> None:
        '''
        '''
        self._c_keypair = getattr(_lib, '%s_keypair' % self._prefix)
        self._c_keypair.argtypes = [_ct.c_char_p, _ct.c_char_p]
        self._c_keypair.restype = None
        self._c_enc = getattr(_lib, '%s_enc' % self._prefix)
        self._c_enc.argtypes = [_ct.c_char_p, _ct.c_char_p, _ct.c_char_p]
        self._c_enc.restype = _ct.c_int
        self._c_dec = getattr(_lib, '%s_dec' % self._prefix)
        self._c_dec.argtypes = [_ct.c_char_p, _ct.c_char_p, _ct.c_char_p]
        self._c_dec.restype = _ct.c_int

    def keypair(self) -> _Tuple[bytes, bytes]:
        '''
        Keypair - randomly generates secret key 'sk' and corresponding public key 'pk'.
        Returns:
            pk (bytes): public key
            sk (bytes): secret key
        '''
        pk = _ct.create_string_buffer(self.PUBLICKEYBYTES)
        sk = _ct.create_string_buffer(self.SECRETKEYBYTES)
        self._c_keypair(pk, sk)
        return pk.raw, sk.raw

    def enc(self, pk: bytes) -> _Tuple[bytes, bytes]:
        '''
        Encapsulation - randomly generates a ciphertext 'c' and the corresponding session key 'k' given Alice's public key 'pk'.
        Parameters:
            pk (bytes): public key
        Returns:
            c (bytes): ciphertext
            k (bytes): session key
        '''
        _check_input(pk, self.PUBLICKEYBYTES, 'pk')
        c = _ct.create_string_buffer(self.CIPHERTEXTBYTES)
        k = _ct.create_string_buffer(self.BYTES)
        pk = _ct.create_string_buffer(pk)
        if self._c_enc(c, k, pk):
            raise Exception('enc failed')
        return c.raw, k.raw

    def dec(self, c: bytes, sk: bytes) -> bytes:
        '''
        Decapsulation - given Alice's secret key 'sk' computes the session key 'k' corresponding to a ciphertext 'c'.
        Parameters:
            c (bytes): ciphertext
            sk (bytes): secret key
        Returns:
            k (bytes): session key
        '''
        _check_input(c, self.CIPHERTEXTBYTES, 'c')
        _check_input(sk, self.SECRETKEYBYTES, 'sk')
        k = _ct.create_string_buffer(self.BYTES)
        c = _ct.create_string_buffer(c)
        sk = _ct.create_string_buffer(sk)
        if self._c_dec(k, c, sk):
            raise Exception('dec failed')
        return k.raw


class mceliece6960119(_KEM):
    PUBLICKEYBYTES = 1047319
    SECRETKEYBYTES = 13948
    CIPHERTEXTBYTES = 194
    BYTES = 32
    _prefix = "mceliece_kem_6960119"


mceliece6960119 = mceliece6960119()


class mceliece6960119f(_KEM):
    PUBLICKEYBYTES = 1047319
    SECRETKEYBYTES = 13948
    CIPHERTEXTBYTES = 194
    BYTES = 32
    _prefix = "mceliece_kem_6960119f"


mceliece6960119f = mceliece6960119f()


class mceliece6960119pc(_KEM):
    PUBLICKEYBYTES = 1047319
    SECRETKEYBYTES = 13948
    CIPHERTEXTBYTES = 226
    BYTES = 32
    _prefix = "mceliece_kem_6960119pc"


mceliece6960119pc = mceliece6960119pc()


class mceliece6960119pcf(_KEM):
    PUBLICKEYBYTES = 1047319
    SECRETKEYBYTES = 13948
    CIPHERTEXTBYTES = 226
    BYTES = 32
    _prefix = "mceliece_kem_6960119pcf"


mceliece6960119pcf = mceliece6960119pcf()


class mceliece6688128(_KEM):
    PUBLICKEYBYTES = 1044992
    SECRETKEYBYTES = 13932
    CIPHERTEXTBYTES = 208
    BYTES = 32
    _prefix = "mceliece_kem_6688128"


mceliece6688128 = mceliece6688128()


class mceliece6688128f(_KEM):
    PUBLICKEYBYTES = 1044992
    SECRETKEYBYTES = 13932
    CIPHERTEXTBYTES = 208
    BYTES = 32
    _prefix = "mceliece_kem_6688128f"


mceliece6688128f = mceliece6688128f()


class mceliece6688128pc(_KEM):
    PUBLICKEYBYTES = 1044992
    SECRETKEYBYTES = 13932
    CIPHERTEXTBYTES = 240
    BYTES = 32
    _prefix = "mceliece_kem_6688128pc"


mceliece6688128pc = mceliece6688128pc()


class mceliece6688128pcf(_KEM):
    PUBLICKEYBYTES = 1044992
    SECRETKEYBYTES = 13932
    CIPHERTEXTBYTES = 240
    BYTES = 32
    _prefix = "mceliece_kem_6688128pcf"


mceliece6688128pcf = mceliece6688128pcf()


class mceliece8192128(_KEM):
    PUBLICKEYBYTES = 1357824
    SECRETKEYBYTES = 14120
    CIPHERTEXTBYTES = 208
    BYTES = 32
    _prefix = "mceliece_kem_8192128"


mceliece8192128 = mceliece8192128()


class mceliece8192128f(_KEM):
    PUBLICKEYBYTES = 1357824
    SECRETKEYBYTES = 14120
    CIPHERTEXTBYTES = 208
    BYTES = 32
    _prefix = "mceliece_kem_8192128f"


mceliece8192128f = mceliece8192128f()


class mceliece8192128pc(_KEM):
    PUBLICKEYBYTES = 1357824
    SECRETKEYBYTES = 14120
    CIPHERTEXTBYTES = 240
    BYTES = 32
    _prefix = "mceliece_kem_8192128pc"


mceliece8192128pc = mceliece8192128pc()


class mceliece8192128pcf(_KEM):
    PUBLICKEYBYTES = 1357824
    SECRETKEYBYTES = 14120
    CIPHERTEXTBYTES = 240
    BYTES = 32
    _prefix = "mceliece_kem_8192128pcf"


mceliece8192128pcf = mceliece8192128pcf()


class mceliece460896(_KEM):
    PUBLICKEYBYTES = 524160
    SECRETKEYBYTES = 13608
    CIPHERTEXTBYTES = 156
    BYTES = 32
    _prefix = "mceliece_kem_460896"


mceliece460896 = mceliece460896()


class mceliece460896f(_KEM):
    PUBLICKEYBYTES = 524160
    SECRETKEYBYTES = 13608
    CIPHERTEXTBYTES = 156
    BYTES = 32
    _prefix = "mceliece_kem_460896f"


mceliece460896f = mceliece460896f()


class mceliece460896pc(_KEM):
    PUBLICKEYBYTES = 524160
    SECRETKEYBYTES = 13608
    CIPHERTEXTBYTES = 188
    BYTES = 32
    _prefix = "mceliece_kem_460896pc"


mceliece460896pc = mceliece460896pc()


class mceliece460896pcf(_KEM):
    PUBLICKEYBYTES = 524160
    SECRETKEYBYTES = 13608
    CIPHERTEXTBYTES = 188
    BYTES = 32
    _prefix = "mceliece_kem_460896pcf"


mceliece460896pcf = mceliece460896pcf()


class mceliece348864(_KEM):
    PUBLICKEYBYTES = 261120
    SECRETKEYBYTES = 6492
    CIPHERTEXTBYTES = 96
    BYTES = 32
    _prefix = "mceliece_kem_348864"


mceliece348864 = mceliece348864()


class mceliece348864f(_KEM):
    PUBLICKEYBYTES = 261120
    SECRETKEYBYTES = 6492
    CIPHERTEXTBYTES = 96
    BYTES = 32
    _prefix = "mceliece_kem_348864f"


mceliece348864f = mceliece348864f()


class mceliece348864pc(_KEM):
    PUBLICKEYBYTES = 261120
    SECRETKEYBYTES = 6492
    CIPHERTEXTBYTES = 128
    BYTES = 32
    _prefix = "mceliece_kem_348864pc"


mceliece348864pc = mceliece348864pc()


class mceliece348864pcf(_KEM):
    PUBLICKEYBYTES = 261120
    SECRETKEYBYTES = 6492
    CIPHERTEXTBYTES = 128
    BYTES = 32
    _prefix = "mceliece_kem_348864pcf"


mceliece348864pcf = mceliece348864pcf()
