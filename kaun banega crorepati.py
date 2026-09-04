# actually we made a program which is in kaon banega crorepati 
print("Welcome to Kaun Banega Crorepati!")

print("what is your name ?")
list = ['(a) amit', '(b) ankit', '(c) anshul', '(d) anshika']
print(list)

name = input("choose correct answer from the list and write :")


if (name == "amit"):
    print("you won 1 crore ")
    print("you are eligible for next question  ")
    print("total balance = 1 crore ")
else:
    print("you lost!")
    print("current balance =0")
    exit()

print("do you want to continue the kaun banega crorepati so type yes otherwise no ")
a=input("type yes or no :")
if(a == "yes"):
    print("Welcome to Kaun Banega Crorepati!")

    print("what is your pet name ?")
    list = ['(a) nikul', '(b) ankur', '(c) kullu', '(d) allu']
    print(list)
    name = input("choose correct answer from the list and write :")
else:
    exit()

if (name == "nikul"):
    print("you won 1 crore ")
    print("you are eligible for next question  ")
    print("total balance = 2 crore ")
else:
    print("you lost!")
    print("current balance =0")