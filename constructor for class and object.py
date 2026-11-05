# consytructor is also work same as before code in class and object 

# a constructor is a special method in a class used to create and initialize an object of class. syntax of python constructors is :
# def __init__(self):
#above is called intialization.

class person:
    def __init__(self ,name,occ):
        print(" hey i am man")
        self.name = name 
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("harry","developer")
b = person("ritik","hk")

a.info()
b.info()
