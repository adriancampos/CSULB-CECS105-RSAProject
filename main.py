import rsa


def main():
    run_debug_stuff()
    """
    A simple menu that allows the user to:
        1. Demo encryption and decryption with a random keypair
        2. Test encryption and decryption with specified integer and length
        3. Generate a keypair
        4. Encrypt
        5. Decrypt
        6. Exit
    Will print to the console the results of each menu choice
    :return: None 
    """
    # Simple menu
    while True:
        print("-----MENU-----")
        print("1. Demo encryption and decryption with a string and a random keypair")
        print("2. Demo encryption and decryption with an integer and specified length")
        print("3. Generate a keypair")
        print("4. Encrypt")
        print("5. Decrypt")
        print("6. Exit")

        choice = input()

        if choice == '1':
            # Demo encryption and decryption with a randomly generated keypair
            demo_rsa_string(input("Enter a string to encrypt and decrypt: "))
        elif choice == '2':
            try:
                demo_rsa_with_integer(int(input("Enter integer message: ")), length=int(input("Enter length: ")))
            except ValueError as e:
                print("Couldn't test (" + str(e) + ")")
        # Generate a keypair
        elif choice == '3':
            try:
                n, e, d = rsa.generate_keys(int(input("Enter desired length: ")))
                print("Modulus (n):\t" + str(n))
                print("Public  (e):\t" + str(e))
                print("Private (d):\t" + str(d))
            except ValueError as e:
                print("Couldn't generate key (" + str(e) + ")")
        # Encrypt
        elif choice == '4':
            try:
                print(
                    "Result:\t" +
                    rsa.encrypt_string_by_parts(
                        input("Input message: "),
                        int(input("Enter the modulus    (n): ")),
                        int(input("Enter the public key (e): "))
                    ))
            # In the event that the user enters a key that doesn't work, alert them
            except ValueError as e:
                print("Invalid key (" + str(e) + ")")
        # Decrypt
        elif choice == '5':
            try:
                print(
                    "Result:\t" +
                    rsa.decrypt_string_by_parts(
                        input("Input ciphertext: "),
                        int(input("Enter the modulus     (n): ")),
                        int(input("Enter the private key (d): "))
                    ))
            # In the event that the user enters a key that doesn't work, alert them
            except ValueError as e:
                print("Invalid key (" + str(e) + ")")
        # Exit
        elif choice == '6':
            break


def demo_rsa_with_integer(message, length):
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
    print()


def demo_rsa_string(message, length=6):
    """
    Generates a keypair, encrypts message with n and e, and decrypts ciphertext with n and d
    :param message: 
    :param length: 
    :return: 
    """
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
    plaintext = rsa.decrypt_string_by_parts(ciphertext, n, d)

    print("-----RESULT-----")
    print(plaintext)


def run_debug_stuff():
    demo_rsa_with_integer(123456, length=8)

main()
