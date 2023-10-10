from mceliece import mceliece6960119f


def test_mceliece6960119f():
    pk, sk = mceliece6960119f.keypair()
    c, k1 = mceliece6960119f.enc(pk)
    k2 = mceliece6960119f.dec(c, sk)
    assert (k1 == k2)
