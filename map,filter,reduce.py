
# this is for map ok.

def cube(x):
    return x*x*x

print(cube(2))
l = [ 2,3,4,6,5]

newl = list(map(cube,l))
print(newl)


# this is for filter ok.
def filter_function(a):
   return a > 2 

newnewl = list(filter(filter_function , l))
print(newnewl)



# this is for reduce 

from functools import reduce 

numbers = [ 1 , 2 , 3 , 4 , 5 ]
# calculate the sum of  the numbers using the reduce function .
def mysum(x,y):
    return x + y 
sum = reduce(mysum , numbers)
print(sum)
               