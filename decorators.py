# Defining the decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()  # This executes your original function
        print("Something is happening AFTER the function is called.")
    return wrapper

# Using the decorator with the '@' symbol
@my_decorator
def say_hello():
    print("Hello, world!")

# Calling the decorated function
say_hello()
