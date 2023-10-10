from mceliece import mceliece348864


def test_mceliece348864():
    pk, sk = mceliece348864.keypair()
    c, k1 = mceliece348864.enc(pk)
    k2 = mceliece348864.dec(c, sk)
    assert (k1 == k2)
