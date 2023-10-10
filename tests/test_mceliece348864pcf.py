from mceliece import mceliece348864pcf


def test_mceliece348864pcf():
    pk, sk = mceliece348864pcf.keypair()
    c, k1 = mceliece348864pcf.enc(pk)
    k2 = mceliece348864pcf.dec(c, sk)
    assert (k1 == k2)
