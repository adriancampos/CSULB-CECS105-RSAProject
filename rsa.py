"""
Contains utility methods to generate keys and encrypt and decrypt messages
Heavily inspired by https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation and Professor John De Sulima-Przyborowski's lectures
"""
import random
import mathutils
import math


def encrypt(message, n, e):
    """
    Encrypts message using Euler's Theorem
    :param message: 
    :param n: 
    :param e: 
    :return: Ciphertext
    """

    # Verify the key is long enough for the encryption to work
    # print(math.log(message))
    # print(n)
    # print(math.log10(message) > math.log10(n))
    if math.log10(message) > math.log10(n):
        raise ValueError("Key length too short")

    # return mathutils.calculate_remainder(message, e, n)  # Traditional Euler's Theorem. Slow with big mod numbers
    return mathutils.calculate_remainder_fast(message, e, n) # Much faster; uses built-in pow() function


def decrypt(ciphertext, d, n):
    """
    Decrypts ciphertext using Euler's Theorem
    :param ciphertext: 
    :param d: 
    :param n: 
    :return: Decrypted message
    """
    # return mathutils.calculate_remainder(ciphertext, d, n)  # Traditional Euler's Theorem. Slow with big mod numbers
    return mathutils.calculate_remainder_fast(ciphertext, d, n)  # Much faster; uses built-in pow() function


def generate_keys(length):
    """
    Generates public and private keys to be used in encrypt and decrypt functions
    :param length: Desired length of the keys
    :return: n, e, d
    """
    # Get two primes, p and q
    p = mathutils.get_random_prime(math.ceil(length / 2))  # The length of p and q is half of total length, since n = pq
    q = mathutils.get_random_prime(math.ceil(length / 2))

    # Encryption breaks if p and q are the same. Ensure that doesn't happen
    while p == q:
        # Keep regenerating q until they're no longer the same
        q = mathutils.get_random_prime(length // 2)

    print("[SECRET] p:\t", p)
    print("[SECRET] q:\t", q)

    # Compute n = pq
    n = p * q
    print("[      ] n:\t", n)

    # Compute λ(n)  (Carmichael's totient function)
    lambda_n = mathutils.totient(p, q)
    print("[SECRET] lambda:\t", lambda_n)

    # Choose any number 1 < e < lambda that is coprime to lambda
    e = -1
    while e == -1 or not mathutils.is_coprime(e, lambda_n):
        e = random.randrange(1, lambda_n - 1)
        # e = 17
    print("[      ] e:\t", e)

    # Find the modular multiplicative inverse of e (modulo λ(n))   (d ≡ e−1 (mod λ(n)))
    d = mathutils.get_mod_mult_inv_euclid(e, lambda_n)
    print("[SECRET] d:\t", d)
    print()

    return n, e, d


def encrypt_string_by_parts(message, n, e):
    """
    Encrypts a string by breaking it into characters, encrypting each integer version of the character, 
    converting each encrypted integer back to an ascii character, and stringing them together  
    :param message: Plaintext message
    :param n: Modulus
    :param e: Public exponent
    :return: Encrypted string
    """
    # Break string into characters to be encrypted
    int_array = [ord(char) for char in message]
    print("Integer form of message:\n" + str(int_array))
    print()

    # Encrypt each item in the array
    print("Encrypting...")
    ciphered_int_array = [encrypt(i, n, e) for i in int_array]

    # Print encrypted integer array as integers separated by a space

    ciphertext = ' '.join([str(i) for i in ciphered_int_array])
    print("Encrypted message:\n" + ciphertext)
    print()

    return ciphertext


def decrypt_string_by_parts(ciphertext, n, d):
    """
    Decrypts a string by breaking it into characters, decrypting each integer version of the character, 
    converting each decrypted integer back to an ascii character, and stringing them together
    :param ciphertext: Encrypted string
    :param n: Modulus
    :param d: Private exponent
    :return: Plaintext, decrypted message
    """
    # Convert ciphertext to int array
    ciphered_int_array = [int(stringed_number) for stringed_number in ciphertext.split(' ')]

    # Decrypt back to plaintext
    print("Decrypting...")
    decrypted_int_array = [decrypt(i, d, n) for i in ciphered_int_array]
    print("Decrypted integer form:\n" + str(decrypted_int_array))
    print()

    # Convert back into ascii
    decrypted_message = ''.join([chr(i) for i in decrypted_int_array])
    print("Decrypted ascii message:\n" + decrypted_message)
    print()

    return decrypted_message
