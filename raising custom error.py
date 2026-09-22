i=int(input("please enter the number between 5 to 9 :"))
if i < 5 or i > 9:
    
    raise ValueError("value should be between 5 and 9")


# in python we can create custom error with the help of raise keyword.

# if we want to write any think in place of value error then we should use class ok .
# otherwise bydefault ValueError will be use otherwise not work ok.


i=int(input("please enter the number between 5 to 9 :"))
if i < 5 or i > 9:
    class UsersDoError(Exception):
        pass

    raise UsersDoError("value should be between 5 and 9")