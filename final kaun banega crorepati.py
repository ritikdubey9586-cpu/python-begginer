question =[ 
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
        break
   

