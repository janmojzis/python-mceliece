from mceliece import mceliece6960119pcf


def test_mceliece6960119pcf():
    pk, sk = mceliece6960119pcf.keypair()
    c, k1 = mceliece6960119pcf.enc(pk)
    k2 = mceliece6960119pcf.dec(c, sk)
    assert (k1 == k2)
