#In Python, access modifiers are used to restrict or permit access to a class's attributes (variables) and methods from outside the class. Unlike languages like Java or C++, Python does not have strict enforcement keywords (like public, private, or protected). Instead, it relies on a naming convention to signal the intended level of access.

#🔑 Key Concepts of Access Modifiers

#• Public Modifiers: Accessible from anywhere (inside the class, outside the class, and in child classes). All variables and methods in Python are public by default.
#• Protected Modifiers: Accessible within the class and its child classes, but should not be accessed from completely outside. They are defined by adding a single underscore (_) prefix. This is a convention (a "gentleman's agreement") and is not strictly blocked by the interpreter.
#• Private Modifiers: Accessible only within the class where they are defined. They are created by adding a double underscore (__) prefix. Python enforces this via a mechanism called Name Mangling, which changes the variable name internally so it cannot be easily accessed from outside.

class Employee:
    def __init__(self, name, salary, project):
        # 1. Public Member: accessible anywhere
        self.name = name
        
        # 2. Protected Member: accessible within class and subclasses
        self._project = project
        
        # 3. Private Member: accessible ONLY within this class
        self.__salary = salary

    # Public method to show private data safely (Getter)
    def display_salary(self):
        return f"Salary: ${self.__salary}"


class Manager(Employee):
    def show_details(self):
        # Can access public and protected members from the subclass
        print(f"Manager Name: {self.name}")
        print(f"Working on Project: {self._project}")
        
        # Trying to access private member here will cause an AttributeError
        # print(self.__salary) 


# ---- Testing the Access Modifiers ----

emp = Employee(name="Alice", salary=85000, project="AI Automation")

# 1. Testing Public
print(emp.name)               # Output: Alice (Accessible directly)

# 2. Testing Protected
print(emp._project)           # Output: AI Automation (Works, but warning/bad practice outside class)

# 3. Testing Private
# print(emp.__salary)         # ❌ Throws AttributeError: 'Employee' object has no attribute '__salary'
print(emp.display_salary())   # Output: Salary: $85000 (Accessed safely via a public method)

# 4. Testing via Subclass
mgr = Manager(name="Bob", salary=120000, project="Cybersecurity")
mgr.show_details()



'''3. Access Modifiers means =

Python uses special naming prefixes to control who can see your variables:
• Public (name): No underscores. Anyone can see it and change it.
• Protected (_name): One underscore. A warning to other coders: "Only use this inside this class or its child classes."
• Private (__name): Two underscores. Strictly locked inside its own class. If you try to call it from outside, Python blocks it and throws an error.'''