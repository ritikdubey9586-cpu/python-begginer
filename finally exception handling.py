
try :
    l=[1,2,3,4,5]
    i=int(input("enter the value : "))
    print(l[i])
except:
    print("there is error ")

    print(" yes you win ")


# here without use of finally last print one also print but they will not print when we use same code in function so for that purpose we make finally ok learn it fastly.

try :
    l=[1,2,3,4,5]
    i=int(input("enter the value : "))
    print(l[i])
except:
    print("there is error ")

finally :
    print(" yes you win ")

# jaise ki hame pta hai jab ham finally likhenge to kuch bhi ho jaye finally vala code confirm print hoga but question ye aata hai ki bina finally likhe bhi to jab ham sirf print use karenge to bhi print ho jayega but fir ek problem aajayegi or vo problem tab ayegi jab ham jab function banayenge 
# now example when we make function 

def ritik():
    try :
        l=[1,2,3,4,5]
        i=int(input("enter the value : "))
        print(l[i])
    except:
        print("there is error ")

        print(" yes you win ")

n = ritik()
print(n)


# dhekha aapne jab hamne function bana ke finally nhi likha to print vala code kaam nhi kiya samjhe aap ki finally ka use karke ham function ke ander bhi except ke baad vale code print kar sakte hai .