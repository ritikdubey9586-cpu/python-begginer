tup=(1,2,3,4,45,6,66,7,78)
print(tup)

print(type(tup))
print(len(tup))
print(tup[0])

print(tup[-3])

print(tup[2])

tup[2]=100

# we cannot change the value of tuple because tuple is immutable.
# here we change the index value of 2 as 100 but it will give an error because tuple is immutable.

#basically we can check any index value of tuple but cant change it.
# actually tuple is immutable and array is not immutable because we can change the value of array but we cannot change the value of tuple.

# all method of list is not applicable in tuple because tuple is immutable and list is mutable.

# example of list method which is not applicable in tuple is append, extend, insert, remove, pop, clear, sort, reverse etc.

# print(tup.reverse)  # This will raise an AttributeError since tuples don't have a reverse method.