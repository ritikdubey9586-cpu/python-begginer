f = open('ritikdubeykafile.txt','r')
print(f)

# this come error this txt file is not exit.
# before run it firstofall we should make the txt file for it where we want to read that file ok 

# dhekho ab usne reaf kiya hai or uske ander ka content print kar diya hai
# but agar hamne file ko close nahi kiya to ye hamare system ke liye problem create kar sakta hai isliye hamesha file ko close karna chahiye
f.close()

# but when we run only these code then whatever content is in the file it will print that content but if we want to read the file line by line then we can use for loop to read the file line by line

text = f.read() # ye hamne file ke ander ka content read kiya hai or usko text variable mein store kar diya hai
print(text) 