import rsa


def main():
    # Demo encryption and decryption with a randomly generated keypair
    demo_rsa_string("Hello world!", length=6)


# TODO Change this to a useful interface
def test_rsa_with_integer(message, length):
    # Generate our keys
    n, e, d = rsa.generate_keys(length)

    print("n:\t" + str(n))
    print("e:\t" + str(e))
    print("d:\t" + str(d))

    print("Original message: " + str(message))

    print("Encrypting {} with public key: n={} | e={}:".format(message, n, e))

    # Encrypt using public key
    ciphertext = rsa.encrypt(message, n, e)

    print("ciphertext: " + str(ciphertext))

    print("Decrypting {} with private key: d={} | n={}:".format(ciphertext, d, n))

    # Decrypt using private key
    decrypted_message = rsa.decrypt(ciphertext, d, n)

    print("decrypted: " + str(decrypted_message))


def demo_rsa_string(message, length):
    # Generate keys
    print("-----GENERATING KEYS-----")
    n, e, d = rsa.generate_keys(length)
    print()
    print("Keys:")
    print("n:\t" + str(n))
    print("e:\t" + str(e))
    print("d:\t" + str(d))
    print()

    # Encrypt
    print("-----ENCRYPTION-----")
    ciphertext = rsa.encrypt_string_by_parts(message, n, e)

    # Decrypt
    print("-----DECRYPTION-----")
    plaintext = rsa.decrypt_string_by_parts(ciphertext, d, n)

    print("-----RESULT-----")
    print(plaintext)


main()
