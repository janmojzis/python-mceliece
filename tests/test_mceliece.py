import mceliece
import os

def test_mceliece():
    kems = []
    for name in dir(mceliece):
        if not name.startswith('mceliece'):
            continue
        kem = getattr(mceliece, name)
        pk, sk = kem.keypair()
        c, k1 = kem.enc(pk)
        k2 = kem.dec(c, sk)
        assert(k1 == k2)
