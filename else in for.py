for i in range(10):
    print(i)

else :
    print("sorry")




# we can use else in while also for example;

i=0
while i>10:
    i= i+1
    print(i)
else :
    print(" you are made ")

# if we used break then else will not work because when we use break that means after break no code will run;

for i in range(10):
    print(i)
    if i==4:
     break
else :
    print("sorry")
