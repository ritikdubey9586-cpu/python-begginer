'''# write a  python program in which message will convert into secret code language.  Use the rules which is mention below if you want to convert normal english into secret code language. 


#coding 
# if the word contains atleast 3 character then remove first letter and append it end of the word  and then append (add) random three letter at starting of the letter 
# else :
#          simply reverse the letter means if word is less than 3 then simply reverse the letters.


#decoding 
# if the words contains less than 3 letter then simply reverse it 
# else :
# remove 3 letter from starting and ending then remove the last letter and append that letter at the starting of the words .
# remove 3 letter from starting and ending then remove the last letter and append that letter at the starting of the words . 


# by using these technique we can easily do coding and decoding 

st = input("enter your message :")
words = st.split(" ")
coding = input(" 1 for coding and 0 for decoding :")
coding = True if coding == "1" else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if len(word) >= 3:
            word = word[1:] + word[0] + "abc"
        else:
            word = word[::-1]
        nwords.append(word)
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            word = word[3:-3]
            word = word[-1] + word[:-1]
        else:
            word = word[::-1]
        nwords.append(word)
    print(" ".join(nwords))'''


# in above code there is one error in decoding part because we have to remove 3 letter from starting and ending then remove the last letter and append that letter at the starting of the words but in above code we are removing 3 letter from starting and ending but we are not removing the last letter and appending that letter at the starting of the words. so i will correct it in below code.

st = input("Enter your message : ")   # yaha pe ham users se message lenge aur usko st variable mein store karenge.
words = st.split(" ")                 # yaha pe ham message ko words mein split karenge aur usko words variable mein store karenge.
coding_input = input("1 for coding and 0 for decoding : ") # yaha pe ham users se coding ya decoding ka input lenge aur usko coding_input variable mein store karenge.
coding = True if coding_input == "1" else False            # yaha pe ham coding_input ko check karenge agar coding_input 1 hai toh coding variable ko True karenge aur agar coding_input 0 hai toh coding variable ko False karenge.

if coding:   # agar coding variable True hai toh niche ka code chalega.
    nwords = [] # yaha pe ham nwords variable ko empty list mein initialize karenge.
    for word in words: # yaha pe ham words variable mein se har word ko iterate karenge.
        if len(word) >= 3:  # agar word ka length 3 ya usse zyada hai toh niche ka code chalega.
            # Pehla letter ko end mein bhejo + "abc" add karo   
            # Pehla letter end mein bhejo + "abc" add karo
            word = word[1:] + word[0] + "abc" # yaha pe ham word ke first letter ko end mein bhejenge aur uske baad "abc" add karenge.
        else: # agar word ka length 3 se kam hai toh niche ka code chalega.
            # Agar 3 se chota hai toh reverse karo
            word = word[::-1]  # yaha pe ham word ko reverse karenge.
        nwords.append(word)    # yaha pe ham nwords list mein word ko append karenge.
    print("Encoded Message:", " ".join(nwords))   # yaha pe ham nwords list ko join karke print karenge.
else:  # agar coding variable False hai toh niche ka code chalega.
    nwords = []  # yaha pe ham nwords variable ko empty list mein initialize karenge.
    for word in words:  # yaha pe ham words variable mein se har word ko iterate karenge.
        if len(word) >= 3:
            # 1. Sabse pehle aakhri ke 3 characters ("abc") ko hatao
            word = word[:-3]
            # 2. Ab jo bacha, uske aakhri letter ko uthakar shuru mein le aao
            word = word[-1] + word[:-1] # yaha pe ham word ke last letter ko uthakar usko starting mein le aayenge aur baaki letters ko uske baad append karenge.
        else:
            # Agar 2 ya kam letter hain toh wapas reverse karo
            word = word[::-1] # yaha pe ham word ko reverse karenge.
        nwords.append(word) # yaha pe ham nwords list mein word ko append karenge.
    print("Decoded Message:", " ".join(nwords)) # yaha pe ham nwords list ko join karke print karenge.
