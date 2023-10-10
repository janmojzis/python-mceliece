from mceliece import mceliece348864pc


def test_mceliece348864pc():
    pk, sk = mceliece348864pc.keypair()
    c, k1 = mceliece348864pc.enc(pk)
    k2 = mceliece348864pc.dec(c, sk)
    assert (k1 == k2)
