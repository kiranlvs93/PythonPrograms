import prime_numbers
from typing import List

factors = []


def least_divisor(dividend, prime_nos):
    """
    Find the least prime divisor for a given number
    :param dividend:
    :param prime_nos:
    :return:
    """
    for divisor in prime_nos:
        if dividend % divisor == 0:
            return divisor


def prime_factors_recursion(number: int, prime_nos: List) -> List:
    """
    This function gives the prime factors of all the given number using recursion
    1. Find the least divisor which has to be one of the prime numbers
    2. Find the quotient
    3. Appends the factors with the divisor
    4. Append the divisor to factors
    5. If quotient is not prime it means we can divide the number further again
    6. Repeat the above steps until the quotient is a prime number
    :param number:
    :param prime_nos:
    :return:
    """
    divisor = least_divisor(number, prime_nos)
    quotient = number // divisor
    factors.append(divisor)
    if quotient not in prime_nos:
        return prime_factors_recursion(quotient, prime_nos)
    else:
        factors.append(quotient)
        return factors


def prime_factors_simple(number: int) -> List:
    """
    This function gives the prime factors of all the given number without recursion
    1. Loop with divisor=2 until the divisor <= the number itself
    2. Check if the dividend is completely divisible by divisor
    3. If true then append the factors with the divisor
    4. Then change the dividend = dividend/divisor
    5. If false then add 1 to the divisor and repeat above steps
    :param number:
    :return:
    """
    factors = []
    divisor = 2
    dividend = number
    print("Hello world")
    while divisor <= dividend:
        if dividend % divisor == 0:
            factors.append(divisor)
            dividend = dividend / divisor
        else:
            divisor += 1
    return factors


if __name__ == '__main__':
    num = 180
    print(prime_factors_recursion(num, prime_numbers.get_prime_numbers(num)[1:]))
    print(prime_factors_simple(num))
