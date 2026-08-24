ritik=["math","english","hindi"]
for x in ritik:
    print(x)




for k in range(1,100):
    print(k)
for k in range(1,100,2):
    print(k)

# here third argument means 2 is for increment the value by 2 from initial value for eaxmple we write (1,100,2)  here start from 1 and direct jump to 2 so next value print 3 simillar next value will be 5 then next will be 7 and continue.
   

n=int(input("enter any number "))
for a in range(1,n):
    print(a)
    if a==1500:
        print("the number is 1500")
    elif a==2000:
        print("the number is 2000")
    elif a==2500:
        print("the number is 2500")
        break



# n is for take input from users for example if user typr 10000
# so for loop will start from 1 as we declare start from 1 and end will whatever users put input so here user is put the last value 10000 so as for loop there is should print of 1 to 10000 but sorry only print 1 to 2500 because when 2500 come loop will stop due to break statement and at 1500 and 2000 it will print the number is 1500 and number is 2000 but loop will not end loop will continue ok when it comes at 2500 then loop will stop due to break statement. 