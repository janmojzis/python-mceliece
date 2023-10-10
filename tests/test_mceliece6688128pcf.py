from mceliece import mceliece6688128pcf


def test_mceliece6688128pcf():
    pk, sk = mceliece6688128pcf.keypair()
    c, k1 = mceliece6688128pcf.enc(pk)
    k2 = mceliece6688128pcf.dec(c, sk)
    assert (k1 == k2)
