l=[1,0,3,4,5,6,7,8]

print(l)

l.append(10)
print(l)

# append is used to add a single element at the end of list.

l.sort()  # when we put only sort then it will sort the list in ascending order be default.
print(l)



l.sort(reverse=True)  # when we put reverse=True then it will sort the list in descending order.
print(l)

l.reverse() # reverse is used to reverse the order of the list.
print(l)

print(l.index(0))
# index is used to find the index of the element in the list.

print(l.count(0))


print(l.copy())

m=l
print(m)



l.insert(2,1000)  # here means add or insert a value of 1000 at index 2 in the list 

# we can also add two list
r=[1,2,3,4,5]
k=[6,7,8,9,10]
p=r+k
print(p)

l.extend(m)

print(l)


# extend is used to add any list in whatever already list make earlier here we extend l list with m ok.
