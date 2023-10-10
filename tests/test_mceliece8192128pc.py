from mceliece import mceliece8192128pc


def test_mceliece8192128pc():
    pk, sk = mceliece8192128pc.keypair()
    c, k1 = mceliece8192128pc.enc(pk)
    k2 = mceliece8192128pc.dec(c, sk)
    assert (k1 == k2)
