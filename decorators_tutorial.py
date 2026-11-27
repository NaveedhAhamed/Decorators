# ==========================================================
# 1. WHAT IS A DECORATOR?
# ==========================================================

# A decorator is a function that takes another function,
# adds or modifies its functionality, and returns a function.

# ==========================================================
# 2. CREATING A BASIC DECORATOR
# ==========================================================

def my_decorator(func):

    def wrapper():
        print("Something happens before the function.")

        func()

        print("Something happens after the function.")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)

say_hello()


# ==========================================================
# 3. USING THE @ DECORATOR SYNTAX
# ==========================================================

def my_decorator(func):

    def wrapper():
        print("Something happens before the function.")

        func()

        print("Something happens after the function.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello from the decorated function!")


say_hello()


# ==========================================================
# 4. DECORATORS WITH ARGUMENTS
# ==========================================================

def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function is about to execute.")

        result = func(*args, **kwargs)

        print("Function has finished executing.")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# ==========================================================
# 5. DECORATORS THAT MODIFY RETURN VALUES
# ==========================================================

def double_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result * 2

    return wrapper


@double_result
def calculate():
    return 10


print(calculate())


# ==========================================================
# 6. DECORATORS FOR EXECUTION TIME
# ==========================================================

import time


def execution_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.4f} seconds")

        return result

    return wrapper


@execution_time
def slow_function():
    time.sleep(2)
    print("Function executed.")


slow_function()


# ==========================================================
# 7. DECORATORS FOR ACCESS CONTROL
# ==========================================================

def check_access(func):

    def wrapper(*args, **kwargs):
        is_admin = True

        if is_admin:
            return func(*args, **kwargs)

        print("Access denied.")

    return wrapper


@check_access
def delete_data():
    print("Data deleted successfully.")


delete_data()


# ==========================================================
# 8. STACKING MULTIPLE DECORATORS
# ==========================================================

def uppercase(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


def add_exclamation(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result + "!"

    return wrapper


@uppercase
@add_exclamation
def greeting():
    return "hello world"


print(greeting())


# ==========================================================
# 9. PRESERVING FUNCTION INFORMATION WITH WRAPS
# ==========================================================

from functools import wraps


def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing function.")

        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet_user():
    """Greets the user."""
    print("Welcome!")


greet_user()

print(greet_user.__name__)
print(greet_user.__doc__)


# ==========================================================
# 10. DECORATORS WITH THEIR OWN ARGUMENTS
# ==========================================================

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hi():
    print("Hi!")


say_hi()


# ==========================================================
# 11. PRACTICAL EXAMPLE: LOGGING FUNCTION CALLS
# ==========================================================

def log_calls(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling function: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished function: {func.__name__}")

        return result

    return wrapper


@log_calls
def multiply(a, b):
    return a * b


print(multiply(5, 4))


# ==========================================================
# 12. PRACTICAL EXAMPLE: CACHING RESULTS
# ==========================================================

def cache_result(func):

    cache = {}

    @wraps(func)
    def wrapper(*args):

        if args in cache:
            print("Using cached result.")
            return cache[args]

        print("Calculating result.")

        result = func(*args)

        cache[args] = result

        return result

    return wrapper


@cache_result
def square(number):
    time.sleep(1)
    return number ** 2


print(square(5))
print(square(5))
print(square(5))


# ==========================================================
# 13. DECORATORS WITH KEYWORD ARGUMENTS
# ==========================================================

def debug(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Returned:", result)

        return result

    return wrapper


@debug
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."


print(introduce("Alex", age=20))
