"""
A helper module with RSA-related maths
"""
import math
import random


def get_random_prime(length):
    """
    Gets a random prime number with specified length 
    :param length: 
    :return: prime number
    """
    while True:
        # Python's built-in random isn't a secure way to generate random numbers. Oh well.
        candidate = random.randrange(10 ** (length - 1), 10 ** length)
        if __is_prime__(candidate):
            return candidate


def __is_prime__(n):
    """
    A probably very inefficient method for checking if a number's prime
    :param n: number to check
    :return: whether the number is prime
    """
    # Highest we need to check is ceil of the square root, plus 1
    for i in range(2, int(math.ceil(n ** 0.5) + 1)):
        # If it's even, it's not prime
        if n % i == 0:
            return False
    # If it makes it all the way through, it's prime
    return True


def gcd(a, b):
    """
    Greatest common divisor of a and b
    :param a: 
    :param b: 
    :return: 
    """
    return math.gcd(a, b)


def lcm(a, b):
    """
    Least common multiple of a and b
    :param a: 
    :param b: 
    :return: 
    """
    return int((a * b) / gcd(a, b))


def totient(p, q):
    """
    Carmichael's/Euler's totient function
    :param p: 
    :param q: 
    :return: 
    """
    # TODO Which totient function to use? Euler's or Carmichael's?
    # Totient of two primes is (p-1) * (q-1)
    # return (p-1) * (q-1)
    return lcm(p - 1, q - 1)


def is_coprime(a, b):
    """
    Determines whether a and b are coprime
    :param a: 
    :param b: 
    :return: 
    """
    return gcd(a, b) == 1


# TODO Get an efficient modular multiplicative inverse algorithm working...
def get_mod_mult_inv(b,n):
    """Wrapper function until I find a mod mult inv function that works well"""
    return get_mod_mult_inv_guess_and_check(b, n)


def get_mod_mult_inv_guess_and_check(b, n):
    """
    This is a terrible modular multiplicative inverse function. Simply tries values until it finds the solution.
    Won't work for moderately large numbers.
    :param b: 
    :param n: 
    :return: 
    """
    test = 0
    while True:
        test += 1
        if b * test % n == 1:
            return test


def get_mod_mult_inv_euler(a, m):
    """
    Finds modular multiplicative inverse using Euler's Theorem
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler.27s_theorem
    Not as fast as Extended Euclid, and actually isn't any faster than brute forcing...
    :param a: 
    :param m: 
    :return: 
    """
    return a ** (phi(m) - 1)


def calculate_remainder_fast(a, exp, m):
    """Calculates (a ** exp) % m efficiently. A wrapper for Python's pow() function"""
    return pow(a, exp, m)

    # Source:
    # number = 1
    # while exp:
    #     if exp & 1:
    #         number = number * a % m
    #     exp >>= 1
    #     a = a * a % m
    # return number


def calculate_remainder(a, exponent, m):
    """
    Calculates remainder of a**exponent % m using Euler's Theorem.
    :param a: 
    :param exponent: 
    :param m: 
    :return: Remainder of a**exponent % m
    """
    # Check to ensure a does not divide m
    if math.gcd(a, m) != 1:
        raise ValueError("gcd(a, m) != 1")

    # Find the congruent exponent (remainder of exponent / phi(m)
    y = exponent % phi(m)

    # Calculate remainder using the congruence
    return (a ** y) % m


def phi(m):
    """
    Euler's Totient function.
    :param m: Any positive integer
    :return: The number of positive integers less than or equal to m and relatively prime to m
    """
    counter = 0

    # Iterate through all numbers between 1 and n inclusive
    for i in range(1, m + 1):
        # If there are no multiples, add one to the counter
        if math.gcd(m, i) == 1:
            counter += 1
    return counter
