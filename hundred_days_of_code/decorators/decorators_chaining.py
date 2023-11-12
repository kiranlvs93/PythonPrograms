import functools


def debug(func):
    """
    Simple decorator to log the called function details
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling function - {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"Result of {func.__name__}({signature}) is {result}")
        return result

    return wrapper


def greet(func):
    """
    Simple decorator
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello", end=' ')
        result = func(*args, **kwargs)
        print(", Hope you are doing fine :-)")
        return result

    return wrapper


def repeat(count):
    """
    Example of a parameterized decorator
    """
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


# Example of chained decorators. The decorators are executed from top to bottom in order of sequence
@debug
@repeat(3)
@greet
def print_name(name):
    print(name, end="")


print_name("Kiran")
