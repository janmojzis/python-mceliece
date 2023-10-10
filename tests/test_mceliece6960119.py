from mceliece import mceliece6960119


def test_mceliece6960119():
    pk, sk = mceliece6960119.keypair()
    c, k1 = mceliece6960119.enc(pk)
    k2 = mceliece6960119.dec(c, sk)
    assert (k1 == k2)
