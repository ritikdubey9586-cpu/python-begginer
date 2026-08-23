name=" !!!!!!!!!!!!! ritik dubey !!!!!!!!!!!!!!"
print(len(name))

print(name.upper())
# this upper is used to change our string into uppercase.

print(name.lower())
# this lower is used to convert string into lowercase.

print(name.rstrip("!"))
# rstrip is used to delete any string whatever you want to delete but this will delete only last one ok.

print(name.replace("ritik" , "airor-1"))
# this replace will work that first it select name and whatever you want to change please mention it in braces like ritik  and write change into which one example ritik , airor-1 
# yaad rakhna comma lagana ritik,airor-1.

print(name.split(" "))
# split is used to make any string into list.


hobby="i like batminton very much"
print(hobby.capitalize())
# capitalize is used to do capital letter only first.

print(name.center(50))
print(hobby.endswith("much"))

# this endswith is used to check whether we mention endswith word is right or wrong if we mention right endswith then compiler will give true.

print(hobby.endswith("much",1,8))
print(hobby.find("much"))
print(name.isalnum())
print(name.isalpha())

print(name.islower())
# islower is used to check that in given string all are in lower case or not.

print(name.isupper())
print(name.isspace())
print(name.istitle())
# title is used to check whether the given string has all word has first letter capital for example.
a="My Name Is Ritik Dubey "
print(a.istitle())

print(name.swapcase())

# swapcase is used to convert all case into one case if all are in lowercase then it will do in upper case  or viseversa.

b="AMIT IS A GOOD BOY"
print(b.swapcase())

