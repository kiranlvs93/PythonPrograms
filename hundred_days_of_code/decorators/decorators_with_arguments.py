"""
This file contains program that shows how to use decorators with arguments
"""


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("********************")
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {func(args)}")

    return wrapper


@logging_decorator
def sum_of_numbers(*args):
    return sum(*args)


@logging_decorator
def multiply(args):
    res = 1
    for a in args:
        res *= a
    return res


sum_of_numbers(1, 2, 3)
multiply(1, 2, 3, 4, 5)
