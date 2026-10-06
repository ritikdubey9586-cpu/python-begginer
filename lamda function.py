# here we are talking about lamda function which means it is one type of anoumous functiuon in which we not use any name 

# as we know that when we make any function then we used def and name of function so if we want to doesnot use def then we used lamda function 

# def double(x)
# return x*2

double = lambda x : x*2
cube = lambda x : x * x * x
avg = lambda x , y , z : (x + y + z)/2


print(double(2))
print(cube(2))
print(avg(3,5,6))

