from mceliece import mceliece348864f


def test_mceliece348864f():
    pk, sk = mceliece348864f.keypair()
    c, k1 = mceliece348864f.enc(pk)
    k2 = mceliece348864f.dec(c, sk)
    assert (k1 == k2)
