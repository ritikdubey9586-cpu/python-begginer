marks =[1,2,3,4,5, 'ritik', 6,7,8]
print(marks)
print(len(marks))
print(type(marks))


print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[6])
print(marks[7])
print(marks[8])
#print(marks[9])

# here we have only 8 index value 9 index is empty or null thatwhy it will give us warning thatswhy i do comment value of index 9 
# index value start always from 0 learn it 

print(marks[-3])      # negative index 
print(marks[len(marks)-3])   # positive index 
print(marks[5-3])       # positive index
print(marks[2])

if 'ritik' in marks:
    print("yes")
else:
    print("no")

if 'ri' in "ritik":
    print("yes you are succesfully launched and you win the game here ")    

# same things apply for string also 
if "ri" in "ritik": 
   print("yes")  
   


print(marks[1:-4])


# listname[start:end:jumpindex]

print(marks[1:8:2])
# here this means start from 1 and end will happen with 8 index value and when start with 1 then 2 index value will not come due to jump index we mention which means they will directly jumped 1 to 3 index value.
lst=[i*i for i in range(10)]
print(lst)


lst=[i*i for i in range(10) if i%2==0]
print(lst)
