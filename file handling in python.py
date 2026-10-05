f = open('ritikdubeykafile.txt','r')  # yaad rakhna sab se pahele ham jo bhi file open karna hai usko likhenge fir uske just bajuy mode likhenge ab mode kafhi hai jaise read ,write ,append etc. or read mode mein ham file ke ander ka content read kar sakte hai or write mode mein ham file ke ander ka content write kar sakte hai or append mode mein ham file ke ander ka content append kar sakte hai
print(f)

# this come error this txt file is not exit.
# before run it firstofall we should make the txt file for it where we want to read that file ok 

# dhekho ab usne reaf kiya hai or uske ander ka content print kar diya hai
# but agar hamne file ko close nahi kiya to ye hamare system ke liye problem create kar sakta hai isliye hamesha file ko close karna chahiye


# but when we run only these code then whatever content is in the file it will print that content but if we want to read the file line by line then we can use for loop to read the file line by line

text = f.read() # ye hamne file ke ander ka content read kiya hai or usko text variable mein store kar diya hai
print(text) 
f.close()


# ek cheese yaad rakhna ki bydefault mode read hota hai to agar hamne mode nahi likha to bhi file read ho jayega but agar hamne write mode ya append mode mein file open kiya to bydefault read mode nahi hoga to hamesha yaad rakhna ki jab bhi ham file open karenge to uske just bajuy mode likhna chahiye
# or ek cheese hamko pta hai agar ham aise file ko read karna chahenge jo exit nhi karta to error ayega but iska ek sio;ution hai python mein ye ki ham aise text file ko bhi rad kar sakte hai uska trick hai read ki jagah write use karo kyuki jaise hi ham write use karenge to vo write function aise file ko create kar dega jo exist nhi karta ok.

#                             code for writing in file
f = open('ritikdubeykafile.txt','w')
f.write('this is my first file handling in python')

f.close()

# yaad rakhna ki jab bhi ham file ko write mode mein open karenge to vo file ke ander ka content delete kar dega or jo bhi hamne write kiya hai vo hi file ke ander ka content hoga but agar ham chahte hai ki file ke ander ka content delete na ho to ham append mode mein file open karenge or fir jo bhi hamne write kiya hai vo file ke ander ka content add ho jayega or pehle se jo bhi content tha vo delete nahi hoga

# agar hame bina delete kiya file mein kuch bhi write karna hai to ham append mode mein file open karenge or fir jo bhi hamne write kiya hai vo file ke ander ka content add ho jayega or pehle se jo bhi content tha vo delete nahi hoga

#                    code for appending in file

f = open('ritikdubeykafile.txt','a')
f.write('this is my first file handling ')
f.close()


# agar ham ye chahte hai ki hame close na likhna ho to ham with open ka use karenge or fir hame close nahi likhna padega kyuki with open ke ander file automatically close ho jayega jaise hi with open ka block khatam ho jayega

with open('ritikdubeykafile.txt','r') as f:
    text = f.read()
    print(text)
