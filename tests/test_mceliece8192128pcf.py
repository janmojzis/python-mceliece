from mceliece import mceliece8192128pcf


def test_mceliece8192128pcf():
    pk, sk = mceliece8192128pcf.keypair()
    c, k1 = mceliece8192128pcf.enc(pk)
    k2 = mceliece8192128pcf.dec(c, sk)
    assert (k1 == k2)
