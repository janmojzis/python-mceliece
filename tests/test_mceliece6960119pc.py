from mceliece import mceliece6960119pc


def test_mceliece6960119pc():
    pk, sk = mceliece6960119pc.keypair()
    c, k1 = mceliece6960119pc.enc(pk)
    k2 = mceliece6960119pc.dec(c, sk)
    assert (k1 == k2)
