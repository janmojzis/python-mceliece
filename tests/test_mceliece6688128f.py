from mceliece import mceliece6688128f


def test_mceliece6688128f():
    pk, sk = mceliece6688128f.keypair()
    c, k1 = mceliece6688128f.enc(pk)
    k2 = mceliece6688128f.dec(c, sk)
    assert (k1 == k2)
