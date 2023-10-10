from mceliece import mceliece460896f


def test_mceliece460896f():
    pk, sk = mceliece460896f.keypair()
    c, k1 = mceliece460896f.enc(pk)
    k2 = mceliece460896f.dec(c, sk)
    assert (k1 == k2)
