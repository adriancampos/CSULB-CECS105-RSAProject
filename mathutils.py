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


def get_mod_mult_inv_euclid(a, m):
    """
    Modular multiplicative inverse of 𝑎 (mod 𝑚) (Finds 𝑥 to satisfy 𝑎𝑥 ≡ 1 (mod 𝑚)) using Extended Euclidean algorithm
    
    From https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm:
    If 𝑎 has a multiplicative inverse modulo 𝑚, this gcd must be 1
    In this case, 𝑎𝑥 + 𝑚𝑦 = gcd(𝑎, 𝑚) = 1
    Which can be rewritten: 𝑎𝑥 - 1 = (-𝑦)𝑚
    Which is: 𝑎𝑥 ≡ 1 (mod 𝑚)
    
    :param a: 
    :param m: 
    :return: 
    """

    # Unpack tuple:
    #     GCD (just to verify)
    #     x: the Bézout coefficient that satisfies 𝑎𝑥 ≡ 1 (mod 𝑚)
    #     y: the other Bézout coefficient. Unused since we're taking mod m
    m_gcd, x, y = extended_euclid_gcd(a, m)

    # Check that the gcd is actually 1
    if m_gcd == 1:
        return x % m
    # If it's not, something's wrong
    else:
        raise ValueError("Modular Multiplicative Inverse: gcd(a, m) != 1")


def extended_euclid_gcd(a, b):
    """
    Finds gcd using the Extended Euclidean Algorithm (ax + by = gcd(a,b))
    Based off of https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Description
    
    :param a: integer a
    :param b: integer b
    :return: (gcd, x, y) such that ax + by = gcd(a,b); x and y are the Bézout coefficients
    """

    # Set up the first two iterations of the sequence
    old_remainder = a  # r₀ = a
    old_s = 1  # s₀ = 1
    old_t = 0  # t₀ = 0

    remainder = b  # r₁ = b
    s = 0  # s₁ = 0
    t = 1  # t₁ = 1

    # Iterate through the rest of the steps. Computation stops once the remainder is 0
    while remainder != 0:
        # Find the whole number result (floor division) of dividing the two numbers in the remainder column
        quotient = old_remainder // remainder

        # Move remainder to old remainder, and compute (and update) the new remainder
        # Could replace 'old_remainder - quotient * remainder' with 'old_remainder % remainder',
        # but since we already spent time to compute the quotient, use it
        old_remainder, remainder = remainder, old_remainder - quotient * remainder

        # Move s to old s, compute new s: sᵢ₊₁ = sᵢ₋₁-qᵢ sᵢ; new s = old_s - q * current_s
        old_s, s = s, old_s - quotient * s

        # Move t to old t, compute new t: tᵢ₊₁ = tᵢ₋₁-qᵢ tᵢ; new t = old_t - q * current_t
        old_t, t = t, old_t - quotient * t

    # Debug print
    if False:
        print("a        : ", a)
        print("b        : ", b)
        print("x (old_s):", old_s)
        print("y (old_t):", old_t)
        print("gcd      :", old_remainder)
        # Confirm that ax + by == gcd(a,b)
        print(a * old_s + b * old_t == old_remainder)

    # Returns a tuple of:
    #     The GCD:
    #         "The greatest common divisor is the last non zero entry [in the remainder column]" (old_remainder)
    #     The Bézout coefficients:
    #         "Bézout coefficients appear in the [s and t columns] of the second-to-last row"
    #         Therefore, they are the last values of s and t, not the most recent (old_s and old_t)
    return old_remainder, old_s, old_t


def get_mod_mult_inv_euler(a, m):
    """
    Finds the modular multiplicative inverse of 𝑎 (mod 𝑚) (Finds 𝑥 to satisfy 𝑎𝑥 ≡ 1 (mod 𝑚)) using Euler's Theorem
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
