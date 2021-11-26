import re


def palindrome(inp):
    """
    Returns boolean based on the given string by checking if its a PALINDROME
    Consider only letters
    Ignore case
    E.g - Palindromes : ABCBA, Race car, RACE CAR, Go hang a salami - I'm a lasagna hog.
          Non palindromes:
    :param inp:
    :return:
    """
    if inp != "quit":
        if any(ch.isdigit() for ch in str(inp)):
            print("Don't enter numbers")
            return False
        else:
            only_alpha = re.compile(r"[a-zA-Z]+")
            inp = "".join(only_alpha.findall(inp))
            return inp == inp[::-1]


if __name__ == '__main__':
    print("Enter any string to check if its PALINDROME or enter quit to exit")
    while True:
        user_inp = input(">>>")
        if user_inp != 'quit':
            print(palindrome(user_inp.lower()))
        else:
            break
