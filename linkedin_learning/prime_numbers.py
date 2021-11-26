from typing import List, Set


def get_prime_numbers(num) -> List:
    """
    Get all the prime nos for a given
    1. Use 2 loops
    2. Outer loop ->i will generate nos until given no
    3. Inner loop ->j will generate nos until nos in the above loop to get the factors
    4. If i%j==0 it means that the j is a factor of i
    5. Add that to the factors list
    6. At any point if factors>2, then its not a prime number. So break out of the inner loop
    7. if the count of factors<=2, then the number is a prime number
    8. Add this number to the prime_nos list and return the list
    :param num:
    :return:
    """
    count_of_factors = 0
    prime_nos = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count_of_factors += 1
            if count_of_factors > 2:
                break
        if count_of_factors <= 2:
            prime_nos.append(i)
        count_of_factors = 0
    return prime_nos


if __name__ == '__main__':
    print(get_prime_numbers(100))
