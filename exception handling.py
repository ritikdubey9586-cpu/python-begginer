a=int(input("please enter any number to count that number as a table "))
print(" the multiplication{a} is : ")
for i in  range(1,11):
    print(f"{a}*{i}={int(a)*i}")

print(" you are succeful")
print(" you are fail ")

# here firstly from above code user enter number and then all line by linre code work and give output but here there is problem when we use string in input means any name then there will be error and when error come then after error come no code will run and no output will come means print (" you are succesful ") bhi nhi chalega 

 # isliye ham exception handling use karenge 



a=int(input("please enter any number to count that number as a table "))
print(" the multiplication{a} is : ")
try :
 for i in  range(1,11):
    print(f"{a}*{i}={int(a)*i}")
except : 
 print(" you entered wrong number ")
print(" you are succeful")
print(" you are fail ")