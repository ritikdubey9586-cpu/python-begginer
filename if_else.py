
'''age = int(input("enter your age "))
if age >=18:
    print("you are eligible")
else:
    print("you are  not eligible")'''

    # nested if else

num=int(input("enter your wish number "))
if (num > 0 and num!=10 and num!=15):
    print("the number is positive")
elif ( num < 0):
    print("the number is negative")
    if (num == 15):
        print("the number is 15")
    else:
        print("the number is not 15")
    if (num == 10):
        print("the number is 10")
    else:
        print("the number is not 10")
else:
    print("the number is zero")