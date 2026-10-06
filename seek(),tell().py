with open('ritikdubeyka new file ','r') as f:
    print(type(f))

    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)

# here seek means check karega jo bhi ham likhenege for example hamne likha 10 to vo starting se 10 word read karega bas 
# or fir jab hamne likha data = f.read(5) 



# we will used truncate and truncate is for placed any string in any pposition

with open('ritikdubey','w') as f :
    f.write('hello everyone my name is ritik dubey and i am ging to develop a system in which anyone can see anyone ok.')
    f.truncate(5)

# by use of truncate we can print any value at any positon 
# for example above example in which firstofall we create a text file in which we placed a string and if i want to print any string from given text fiule so at that we used truncate ok.