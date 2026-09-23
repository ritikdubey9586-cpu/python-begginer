'''question =[ 
[ "which language is used to create facebook ?", "python","java","c","c++","none",4],
[ "which language is used to create instagram ?", "python","java","c","c++","none",4],
[ "which language is used to create mysql    ?", "python","java","c","c++","none",4],
[ "which language is used to create youtube?", "python","java","c","c++","none",4],
[ "which language is used to create flipkart ?", "python","java","c","c++","none",4],
]

levels =[1000,2000,3000,4000,5000,10000,20000,30000,40000,50000,100000,200000,300000,500000]

for i in range (0,len(question)):
    question =question[i]
    print(f"question for rs.{levels[i]}")
    print(f" a. {question[1]}                      b. {question[2]}")
    print(f" c. {question[3]}                      d. {question[4]}")

    reply= int(input(" enter your answe (1-4)"))
    if( reply == question[-1]):
        print(f" answer is correct ,you have won rs.{levels[i]}")
        if(i==4):
            money = 10000
        elif (i== 9):
            money = 100000
        elif ( i== 14):
            money = 300000  
    
    else:
        print("wrong answer ")
        break'''
   
# in above code there is error that'why i fix it and rewrite below so learn lower code ok.
question = [ 
    ["Which language is used to create Facebook?", "Python", "Java", "C", "C++", "None", 4],
    ["Which language is used to create Instagram?", "Python", "Java", "C", "C++", "None", 1], # Instagram mostly Python/Django pe hai
    ["Which language is used to create MySQL?", "Python", "Java", "C", "C++", "None", 4],   # MySQL C/C++ mein likha hai
    ["Which language is used to create YouTube?", "Python", "Java", "C", "C++", "None", 1], # YouTube ka back-end heavy Python hai
    ["Which language is used to create Flipkart?", "Python", "Java", "C", "C++", "None", 2], # Flipkart Java use karta hai
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 500000]

money = 0 # Won money ko track karne ke liye variable pehle declare kiya

for i in range(0, len(question)):
    # ERROR FIXED: Humne variable ka naam badal kar 'q' kar diya taaki list overwrite na ho
    q = question[i] 
    
    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"{q[0]}") # Sawal print karne ke liye
    print(f" a. {q[1]}                      b. {q[2]}")
    print(f" c. {q[3]}                      d. {q[4]}")

    reply = int(input("Enter your answer (1-4): "))
    
    # Sahi answer check kar rahe hain
    if reply == q[-1]:
        print(f"Answer is correct! You have won Rs.{levels[i]}")
        
        # Safe money levels update karne ke liye logic
        if i == 4:
            money = 5000
        elif i == 9:
            money = 50000
    else:
        print("Wrong answer!")
        print(f"You take home: Rs.{money}") # Agar galat hua toh safe money milega
        break
