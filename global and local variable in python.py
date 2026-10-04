x = 10 # global variable



def my_function():
    global x # global variable ko access karne ke liye global keyword ka use karenge.
    x = 5 # global variable ko change karenge
    y = 20 # local variable
my_function() # function ko call karenge

print(x) # local variable ko print karenge
print(y) # local variable ko print karenge



# hamesa yaad rakhna jab ham koi function bana ke function ke ander kisi bhi variable ko likhte hai to vo variable local variable hoga
# global variable ko function ke bahar  access kiya jata  hai
# or ek cheese ham log global variable ko function ke ander bhi access kar sakte hai but local variable ko function ke bahar access nahi kar sakte hai
# jaise ki upar ke code mein hamne global variable x ko function ke ander access kiya hai or local variable y ko function ke bahar access nahi kar sakte hai
# dhekho pahele hi hamne function ke andar likh diya ki variable x ko global variable ke roop mein use karenge to ham function ke ander bhi global variable x ko access kar sakte hai or change bhi kar sakte hai
# or hamne y variable ke liye function mein kuch nahi likha to y variable local variable ban gaya or ham function ke bahar y variable ko access nahi kar sakte hai

# tum dhek sakte ho jaise hi maine print(x) likha to answer aagaya but jaise hi print(y) likha to error aagaya ki y variable is not defined

