"""
Count the minimum number of coins that must be reversed to achieve a sequence of alternating heads and tails.
"""


def flips_second(coinss):
    flips = 0
    for i in range(0, len(coinss) - 1):
        if coinss[i] == coinss[i + 1]:
            coinss[i + 1] = not coinss[i + 1]
            flips += 1
    return flips


def flips_first(coinss):
    flips = 0
    for i in range(0, len(coinss) - 1):
        if coinss[i] == coinss[i + 1]:
            coinss[i] = not coinss[i]
            flips += 1
    return flips


# print(min(flips_first(coins.copy()), flips_second(coins.copy())))


def solution(A):
    flips1 = sum(n == i % 2 for i, n in enumerate(A))
    flips2 = sum(n == (i + 1) % 2 for i, n in enumerate(A))
    return min(flips1, flips2)


# coins = [0, 1, 1, 0]
# coins = [1, 0, 1, 0, 1, 1]
# coins = [1, 1, 0, 1, 1]
# coins = [0, 1, 0]
coins = [1, 1, 1, 1]
print(solution(coins))
