import os 

#if not os.path.exists("day"):
   # os.mkdir("day")

for i in range(1,100) :
    #os.mkdir(f"day/{i}")

# with  the help of os means operating system we can crete folder and subfolder in python and we can do many more things with the help of os module in python.

# above code is for create 100 folder in day folder with the help of os module in python.

# now if we want to rename the folder name then we can use os.rename() function in python.

 os.rename("day/2", f"day/day_{i}")

 # there are many more functions in os module in python like os.remove() to remove the file or folder, os.listdir() to list the files and folders in a directory, os.getcwd() to get the current working directory, os.chdir() to change the current working directory, etc.

# listdir karke ki os module mein function hai jisse hum directory ke andar ke files aur folders ko list kar sakte hai.
files = os.listdir("day")