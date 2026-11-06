class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # '_' ka matlab hai yeh ek private/protected variable hai

    # GETTER: Iske zariye hum '_age' ki value ko read karenge
    @property
    def age(self):
        print("Getter method called")
        return self._age

    # SETTER: Iske zariye hum validation check lagakar value edit karenge
    @age.setter
    def age(self, value):
        print(f"Setter method called with value: {value}")
        # Validation: Age kabhi bhi 0 ya negative nahi ho sakti
        if value <= 0:
            print("Error: Age cannot be 0 or negative!")
        else:
            self._age = value

# ---- Code Running Execution ----

s1 = Student("Ritik", 20)

# 1. Getter automatically call hoga (Bina parenthesis '()' ke use kiye)
print(s1.age)  

print("-" * 30)

# 2. Setter automatically call hoga jab hum value change karenge
s1.age = 25  # Valid age change
print(s1.age)

print("-" * 30)

# 3. Invalid change checking (Validation rule trigger hoga)
s1.age = -5  # Yeh validation rule fail kar dega
print(s1.age)  # Old age (25) hi rahegi, change nahi hogi
