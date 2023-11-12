"""
This file contains program that shows how to use decorators with arguments

The general syntax is as below

def my_decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        #do something before the function
        result = function(*args)
        #do something after the function
        return result
    return wrapper
"""
import functools


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("********************")
        print(f"You called {func.__name__}{args}")
        result = func(args)
        print(f"It returned: {result}")
        return result

    return wrapper


def repeat(num_of_times):
    """
    Decorator with argument
    """
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Repeating the function {num_of_times} times")
            for _ in range(num_of_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@logging_decorator
def sum_of_numbers(*args):
    return sum(*args)


@logging_decorator
def multiply(*args):
    """
    Numbers to be multiplied
    """
    res = 1
    for a in args[0]:
        res *= a
    return res


@repeat(10)
def greet(name):
    print(f"Hello {name}!!")


s = sum_of_numbers(1, 2, 3)
m = multiply(1, 2, 3, 4, 5)
print(f"{sum_of_numbers.__name__=}")
print(f"{help(multiply)}")
greet("Elon Musk")
