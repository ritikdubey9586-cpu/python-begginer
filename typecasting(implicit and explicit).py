a="1"
b="2"
print(a+b)
# here a="1" this is string and b="2" is also string thatwhy compiler didnot add both value just right as a string like a="harry" and b="ritik"


# there are two type of conversion :
# (1) explicit and (2) implicit 

# for explicit conversion
a="1"
b="2"
print(int(a) + int(b))

# in explicit we forcefully convert this string into integer and then compiler can add this code 

# for implicit conversion

a=1.2
b=2
print(a+b)

# here compiler automatic convert because there is no need to convert a is float while b is int but we are not doing forcefully conversion thatswhy it is called implicit conversion.
