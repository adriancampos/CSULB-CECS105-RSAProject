import rsa

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


def perform_rsa_string(message, length):
    print("Original message:\n" + message)
    print()

    # Break string into characters to be encrypted
    int_array = [ord(char) for char in message]
    print("Integer form of message:\n" + str(int_array))
    print()

    # TODO move this
    # Generate keys
    print("Generating keys...")
    n, e, d = rsa.generate_keys(length)
    print("n:\t" + str(n))
    print("e:\t" + str(e))
    print("d:\t" + str(d))

    # Encrypt each item in the array
    print("Encrypting...")
    ciphered_int_array = [rsa.encrypt(i, n, e) for i in int_array]
    print("Ciphertext:\n" + str(ciphered_int_array))
    print()

    # Decrypt back to plaintext
    print("Decrypting...")
    decrypted_int_array = [rsa.decrypt(i, d, n) for i in ciphered_int_array]
    print("Decrypted integer form:\n" + str(decrypted_int_array))
    print()

    # Convert back into ascii
    decrypted_message = ''.join([chr(i) for i in decrypted_int_array])
    print("Decrypted ascii message:\n" + decrypted_message)
    print()






perform_rsa_string("Hello world!", length = 4)





# test_rsa_with_integer(108, length=4)




