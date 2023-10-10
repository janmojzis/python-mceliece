from mceliece import mceliece460896pc


def test_mceliece460896pc():
    pk, sk = mceliece460896pc.keypair()
    c, k1 = mceliece460896pc.enc(pk)
    k2 = mceliece460896pc.dec(c, sk)
    assert (k1 == k2)
