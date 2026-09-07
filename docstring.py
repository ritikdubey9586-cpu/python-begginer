def square(num):
    """This function takes a number as input and returns the square of that number."""
    return num ** 2

print(square(5))  # Output: 25
print(square.__doc__)  # Output: This function takes a number as input and returns the square of that number.

# basically we used """ """ this is used for doc string purpose and we can used as a comment also but when we not write doc string then we can used ok




# another example of docstrings 

def calculate_area(width, height):
    """Calculate the area of a rectangle from its width and height."""
    return width * height

# 1. Calling the function normally
print(calculate_area(5, 10))  # Output: 50

# 2. Accessing the documentation we wrote inside the function
print(calculate_area.__doc__)  # Output: Calculate the area of a rectangle from its width and height.