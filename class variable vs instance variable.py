class Student:
    # 1. Class Variable (Sabhi students ke liye same rahega)
    school_name = "ABC High School"

    def __init__(self, name, age):
        # 2. Instance Variables (Har student ka alag hoga)
        self.name = name
        self.age = age

# Do alag-alag objects (instances) banana
s1 = Student("Rahul", 15)
s2 = Student("Amit", 16)

# Instance variables ko access karna (Dono ki values alag hain)
print(s1.name, s1.age)  # Output: Rahul 15
print(s2.name, s2.age)  # Output: Amit 16

# Class variable ko access karna (Dono ke liye same hai)
print(s1.school_name)   # Output: ABC High School
print(s2.school_name)   # Output: ABC High School

# Class variable ko directly Class name se bhi access kar sakte hain
print(Student.school_name)  # Output: ABC High School
