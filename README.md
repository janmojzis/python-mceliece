Python wrapper around implementation of the Classic McEliece cryptosystem.

To access the Python functions provided by mceliece, import the library (for, e.g., mceliece6960119):

    from mceliece import mceliece6960119

To generate a key pair:

    pk,sk = mceliece6960119.keypair()

To generate a ciphertext c encapsulating a randomly generated session key k:

    c,k = mceliece6960119.enc(pk)

To recover a session key from a ciphertext:

    k = mceliece6960119.dec(c,sk)

As a larger example, the following test script creates a key pair, creates a ciphertext and session key, and then recovers the session key from the ciphertext:

    import mceliece
    kem = mceliece.mceliece6960119
    pk,sk = kem.keypair()
    c,k = kem.enc(pk)
    assert k == kem.dec(c,sk)
