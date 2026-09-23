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


'''Code Ka Ek-Ek Line Explanation (Line-by-Line)Chalo code ki ek-ek line ko shuru se dekhte hain:
1. Sawalon ki List (Questions Data)pythonquestion = [ 
    ["Which language is used to create Facebook?", "Python", "Java", "C", "C++", "None", 4],
Use code with caution.Kya ho raha hai? Yeh ek badi list ([ ]) hai jismein 5 choti lists hain.
 Isko programming mein 2D List kehte hain.Ek list ka post-mortem: ["Which language...", "Python", "Java", "C", "C++", "None", 4]Index 0: "Which language..." (Yeh sawal hai)Index 1: "Python" (Option A)Index 2: "Java" (Option B)Index 3: "C" (Option C)Index 4: "C++" (Option D)Index 5: "None" (Option E - Yaani upar ka koi nahi)Index 6 ya [-1]: 4 (Yeh Correct Answer ka number hai. Iska matlab is sawal ka sahi jawab Index 4 yaani C++ hai).2. Rakam ki List (Prize Money)pythonlevels = [1000, 2000, 3000, 4000, 5000]
Use code with caution.Kya ho raha hai? Yeh simple list hai jo har sawal ke liye milne wale paise track karti hai. Pehla sawal sahi hua toh Rs. 1000, dusra toh Rs. 2000, aese hi aage tak.3. Safe Money Variablepythonmoney = 0
Use code with caution.Kya ho raha hai? Humne ek variable banaya money naam ka aur shuru mein use 0 value de di. Yeh KBC ke padav (safe zone) ki tarah kaam karega. Agar user beech mein game haarega, toh use yeh safe money milegi.4. Loop ki Shuruatpythonfor i in range(0, len(question)):
Use code with caution.Kya ho raha hai? len(question) ka matlab hai total sawal (jo ki 5 hain). range(0, 5) ka matlab hai yeh loop 5 baar chalega.Pehli baar chalne par i ki value 0 hogi, dusri baar 1, teesri baar 2, aese hi 4 tak jayegi.5. Current Question ko Alag Karna (Yahan Error Fix Kiya)python    q = question[i]
Use code with caution.Kya ho raha hai? Jab loop pehli baar chalega (i=0), toh question[0] (yaani pehla sawal aur uske options) uth kar q naam ke naye variable mein aa jayenge.Pehle tumne yahan question = question[i] likha tha, jisse poori list hi delete ho jati thi. Ab q likhne se poori list surakshit hai.6. Screen par Sawal aur Amount Dikhanapython    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"{q[0]}")
Use code with caution.Kya ho raha hai?Pehli line print karegi: Question for Rs.1000 (Kyunki levels[0] par 1000 hai).Dusri line print karegi sawal: q[0] ka matlab hai q list ka pehla element, jo ki sawal ka text hai.7. Options ko Screen par Print Karnapython    print(f" a. {q[1]}                      b. {q[2]}")
    print(f" c. {q[3]}                      d. {q[4]}")
    print(f" e. {q[5]}")  # NONE YAHAN PRINT HOGA!
Use code with caution.Kya ho raha hai?q[1] se Python print hoga, q[2] se Java, q[3] se C, q[4] se C++.Aur agar tumhein None bhi dikhana hai, toh humne q[5] ko option e. bana kar print kar diya.8. User se Answer Lenapython    reply = int(input("Enter your answer (1-5): "))
Use code with caution.Kya ho raha hai? input() user se keyboard par type karwayega. User jo bhi type karega (jaise 4), use int() ki madad se integer (number) mein badal kar reply variable mein save kar diya jayega. Kyunki humne None ko 5th option banaya hai, isliye humne message mein (1-5) likha hai.9. Answer Sahi hai ya Galat Check Karnapython    if reply == q[-1]:
Use code with caution.Kya ho raha hai? Python mein [-1] ka matlab hota hai list ka aakhri element. Hamari list ka aakhri element sahi jawab ka number hai (jaise pehle sawal ke liye 4). Yeh line check kar rahi hai ki kya user ka reply aur sahi jawab q[-1] barabar hain?10. Sahi Jawab Hone Par Kya Hogapython        print(f"Answer is correct! You have won Rs.{levels[i]}")
        
        if i == 4:
            money = 5000
Use code with caution.Kya ho raha hai? Agar jawab sahi hai, toh screen par badhai ka message aayega. Uske baad hum check kar rahe hain ki kya yeh aakhri sawal tha (i == 4)? Agar haan, toh money variable mein Rs. 5000 safe kar diye jayenge.11. Galat Jawab Hone Par (Else Condition)python    else:
        print("Wrong answer!")
        print(f"You take home: Rs.{money}")
        break'''