import time 

t=(time.strftime("%H:%M:%S"))
print(t)

# this is for what time exactly in your pc live ok 

# now we write a code for take users input if users type any time then he or she will get the welcome message whaterver time he or she mentioned .

hour=time.strftime("%H")
hour=int(input("Enter the hour in 24 hour format: "))
print(hour)


if (hour>=0 and hour<12):
    print("good morning")
elif (hour>=12 and hour<16):
    print("good afternoon")
elif (hour>=16 and hour<20):
    print("good evening")
elif (hour>=20 and hour<24):
    print("good night:")
else:
    print("no answer ! ")



