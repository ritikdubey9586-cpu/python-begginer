# this is a project where user can find out the greeting according to time
# if he goes for buy vegetable and he dont know what time and at that time one sir came and then form my project he saw and say good morning or good evening or good afternoon.
import time

# 1. strftime("%H") se current hour nikala aur use integer me badla
current_hour = int(time.strftime("%H"))

# 2. Question ke mutabiq 3 greetings lagaye
if current_hour < 12:
    print("Good Morning")
elif current_hour < 17:  # 12 PM se 5 PM ke beech
    print("Good Afternoon")
else:                    # 5 PM ke baad ka poora time
    print("Good Evening")


# is question mein dhekho kya ho rha hai 
# sabse pahele ye question main import time se ham abhi apne laptop mein current time kya ho rha pta chalta hai 
# uske baad line 4 per jo hai current_hour = int(time.strftime("%H")) ismein execution start hota hai time.strftime("%H") se matlab abhu current mein pc mein jo  hour ho rha hoga vo batayega jaise 10 fir ye 10 ek string hai because hamne strf use kiya fir ye convert hoga int mein by use of int .
# then current_hour ek dabba cretae karega jismein vo ye value ko store karega fir aage command check hoga jo time ho rha hoga vo i and elif se check hoga fir print ho jayega. 