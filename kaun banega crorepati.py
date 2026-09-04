# actually we made a program which is in kaon banega crorepati 

from matplotlib.pyplot import show


print("Welcome to Kaun Banega Crorepati!")

print("what is your name ?")
list = ["(a) amit", "(b) ankit", "(c) anshul", "(d) anshika"]

name = input("choose correct answer from the list and write :")


if (name == "amit"):
    print("you won 1 crore ")
    print("you are eligible for next question  ")
    print("total balance = 1 crore ")
else:
    print("you lost!")
    print("current balance =0")

show = input("do you want to play again ? (yes/no) : ")
show()

if (show == "yes"):
    print("Welcome to Kaun Banega Crorepati!")

    print("what is your pet name ?")
    list = ["(a) amit", "(b) ankit", "(c) anshul", "(d) anshika"]

    name = input("choose correct answer from the list and write :")


    if (name == "amit"):
        print("you won 1 crore ")
        print("you are eligible for next question  ")
        print("total balance = 1 crore ")
    else:
        print("you lost!")
        print("current balance =0")