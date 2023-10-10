from mceliece import mceliece8192128f


def test_mceliece8192128f():
    pk, sk = mceliece8192128f.keypair()
    c, k1 = mceliece8192128f.enc(pk)
    k2 = mceliece8192128f.dec(c, sk)
    assert (k1 == k2)
