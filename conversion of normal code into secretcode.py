# write a  python program in which message will convert into secret code language.  Use the rules which is mention below if you want to convert normal english into secret code language. 


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
    print(" ".join(nwords))
    

