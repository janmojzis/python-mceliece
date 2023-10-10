from mceliece import mceliece6688128


def test_mceliece6688128():
    pk, sk = mceliece6688128.keypair()
    c, k1 = mceliece6688128.enc(pk)
    k2 = mceliece6688128.dec(c, sk)
    assert (k1 == k2)
