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

st = input("Enter your message : ")
words = st.split(" ")
coding_input = input("1 for coding and 0 for decoding : ")
coding = True if coding_input == "1" else False

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            # Pehla letter end mein bhejo + "abc" add karo
            word = word[1:] + word[0] + "abc"
        else:
            # Agar 3 se chota hai toh reverse karo
            word = word[::-1]
        nwords.append(word)
    print("Encoded Message:", " ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            # 1. Sabse pehle aakhri ke 3 characters ("abc") ko hatao
            word = word[:-3]
            # 2. Ab jo bacha, uske aakhri letter ko uthakar shuru mein le aao
            word = word[-1] + word[:-1]
        else:
            # Agar 2 ya kam letter hain toh wapas reverse karo
            word = word[::-1]
        nwords.append(word)
    print("Decoded Message:", " ".join(nwords))
