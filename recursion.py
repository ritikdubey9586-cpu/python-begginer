# this is code for recursion which means a function calling itself to solve a problem. Recursion is a powerful technique in programming that allows for elegant solutions to complex problems. It is often used in algorithms that involve tree structures, backtracking, and divide-and-conquer strategies.


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

n = int(input("Enter a number to find its factorial: "))
print(factorial(n))




# we do program for fibonacci series with help of recursion.

def fibonacci(a):
    if ( a == 0 or a== 1):
        return a
    else :
        return  fibonacci(a-1) + fibonacci(a-2)
    

print(fibonacci(5))






