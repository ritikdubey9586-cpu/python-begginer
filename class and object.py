# we are writing a code for class in which we mentioned a class and by using that class we can edit different different person.
# a class is blueprint or template for creating objects.
class info:
    name = "ritik"
    surname = " dubey "
    occupation = "ethical hackers "

    # FIXED: This function must be indented inside the class block
    def details(self):
        # FIXED: Added self.name to the print statement so it uses the dynamic name
        print(f"my name is {self.name} {self.surname} and i am a {self.occupation}")

a = info()
b = info()

# Editing person A
a.name = "amit"
a.surname = "yadav"
a.occupation = "bank manager"

# Now both will run perfectly!
a.details()
b.details()
