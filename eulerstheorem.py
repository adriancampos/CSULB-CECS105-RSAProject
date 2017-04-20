import sys
import math


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


# A simple interface that'll be used if this file is run on its own
if __name__ == "__main__":
    try:
        # Calculate the remainder of three integers passed as parameters
        print(calculate_remainder(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    except (IndexError, ValueError):
        # If the user passed the incorrect number of parameters, alert them and use default, hardcoded numbers
        print("Must pass three integers. Using default: 245**1040 / 18.")
        print(calculate_remainder(245, 1040, 18))
