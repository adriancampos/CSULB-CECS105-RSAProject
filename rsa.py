"""
Contains utility methods to generate keys and encrypt and decrypt messages
Heavily inspired by https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation and Professor John De Sulima-Przyborowski's lectures
"""
import random
import mathutils


def encrypt(message, n, e):
    """
    Encrypts message using Euler's Theorem
    :param message: 
    :param n: 
    :param e: 
    :return: Ciphertext
    """
    return mathutils.calculate_remainder(message, e, n)
    # return pow(message, e, n) # Seems to be faster


def decrypt(ciphertext, d, n):
    """
    Decrypts ciphertext using Euler's Theorem
    :param ciphertext: 
    :param d: 
    :param n: 
    :return: Decrypted message
    """
    return mathutils.calculate_remainder(ciphertext, d, n)
    # return pow(ciphertext, d, n) # Seems to be faster


def string_to_decimal(message: str):
    # TODO This is super ugly.
    return int(''.join([str(hex(ord(char))[2:]) for char in message]), 16)


def decimal_to_string(message: int):
    # TODO Complete this
    return "Null"


def generate_keys(length):
    """
    Generates public and private keys to be used in encrypt and decrypt functions
    :param length: Desired length of the keys
    :return: n, e, d
    """
    # Get two primes, p and q
    p = mathutils.get_random_prime(length // 2)  # The length of p and q is half of the total length, since n = pq
    q = mathutils.get_random_prime(length // 2)

    # Encryption breaks if p and q are the same. Ensure that doesn't happen
    while p==q:
        # Keep regenerating q until they're no longer the same
        q = mathutils.get_random_prime(length // 2)

    print("Found p and q")
    # p = 61
    # q = 53

    # Compute n = pq
    n = p * q

    # Compute λ(n)  (Carmichael's totient function)
    lambda_n = mathutils.totient(p, q)
    print("Computed totient")

    # Choose any number 1 < e < lambda that is coprime to lambda
    e = -1
    while e == -1 or not mathutils.is_coprime(e, lambda_n):
        e = random.randrange(1, lambda_n - 1)
        # e = 17
    print("Found e")

    # Find the modular multiplicative inverse of e (modulo λ(n))   (d ≡ e−1 (mod λ(n)))
    d = mathutils.get_mod_mult_inv(e, lambda_n)
    print("Found d")

    return n, e, d
