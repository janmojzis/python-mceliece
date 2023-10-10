from mceliece import mceliece460896pcf


def test_mceliece460896pcf():
    pk, sk = mceliece460896pcf.keypair()
    c, k1 = mceliece460896pcf.enc(pk)
    k2 = mceliece460896pcf.dec(c, sk)
    assert (k1 == k2)
