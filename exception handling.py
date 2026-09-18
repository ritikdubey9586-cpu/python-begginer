a=int(input("please enter any number to count that number as a table "))
print(" the multiplication{a} is : ")
for i in  range(1,11):
    print(f"{a}*{i}={int(a)*i}")

print(" you are succeful")
print(" you are fail ")

# here firstly from above code user enter number and then all line by linre code work and give output but here there is problem when we use string in input means any name then there will be error and when error come then after error come no code will run and no output will come means print (" you are succesful ") bhi nhi chalega 

 # isliye ham exception handling use karenge 



a=int(input("please enter any number to count that number as a table "))
print(" the multiplication{a} is : ")
try :
 for i in  range(1,11):
    print(f"{a}*{i}={int(a)*i}")
except : 
 print(" you entered wrong number ")
print(" you are succeful")
print(" you are fail ")

def divide_numbers():
    try:
        # Aisa code jo error generate kar sakta hai
        numerator = int(input("Enter the first number (Numerator): "))
        denominator = int(input("Enter the second number (Denominator): "))
        
        result = numerator / denominator

    except ZeroDivisionError:
        # Jab denominator me 0 daala jaye
        print("Error: Aap kisi bhi number ko zero (0) se divide nahi kar sakte!")
        
    except ValueError:
        # Jab user number ki jagah text ya alphabet daal de
        print("Error: Kripya sirf valid numbers (integers) hi enter karein!")
        
    except Exception as e:
        # Koi bhi dusra anjaan error handle karne ke liye
        print(f"Ek unexpected error aaya: {e}")
        
    else:
        # Ye tab chalega jab try block me koi error NAHI aayega
        print(f"Success! Aapka answer hai: {result}")
        
    finally:
        # Ye block humesha chalega, chahe error aaye ya na aaye
        print("Execution complete. Thank you!")

# Function ko chalane ke liye:
divide_numbers()

