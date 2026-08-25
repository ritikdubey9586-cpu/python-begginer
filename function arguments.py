def average(a=None, b=None):
    if a is None:
        a = int(input("enter any value of a : "))
    if b is None:
        b = int(input("enter any value of b : "))
    result = (a + b) / 2
    print("the average of a and b ", result)

average(5,6)


# basically when we write average to get output of our user defined function then answer will come but we can change the argument also ok and we can change augument any one also.

'''def average(a=None, b=None):
    # If 'a' is not passed, ask the user for input
    if a is None:
        a = int(input("enter any value of a : "))
        
    # If 'b' is not passed, ask the user for input
    if b is None:
        b = int(input("enter any value of b : "))

    # These lines MUST have 4 spaces of indentation to stay inside the function
    result = (a + b) / 2
    print("the average of a and b ", result)
    
# --- Test it out below ---

# Case 1: Ask user for both values
# average()

# Case 2: Pass both values directly (no inputs asked)
average(5, 6)

# Case 3: Pass only one value (will only ask input for 'b')
# average(a=10)'''
