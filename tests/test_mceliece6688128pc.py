from mceliece import mceliece6688128pc


def test_mceliece6688128pc():
    pk, sk = mceliece6688128pc.keypair()
    c, k1 = mceliece6688128pc.enc(pk)
    k2 = mceliece6688128pc.dec(c, sk)
    assert (k1 == k2)
