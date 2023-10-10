from mceliece import mceliece8192128


def test_mceliece8192128():
    pk, sk = mceliece8192128.keypair()
    c, k1 = mceliece8192128.enc(pk)
    k2 = mceliece8192128.dec(c, sk)
    assert (k1 == k2)
