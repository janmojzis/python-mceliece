from mceliece import mceliece460896


def test_mceliece460896():
    pk, sk = mceliece460896.keypair()
    c, k1 = mceliece460896.enc(pk)
    k2 = mceliece460896.dec(c, sk)
    assert (k1 == k2)
