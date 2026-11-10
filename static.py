 # A static method in Python is a function inside a class that does not require an instance of the class to run.
 # Unlike regular methods, it does not take self or cls as its first parameter. This means it cannot modify the state of an object or the class itself. It behaves exactly like a normal function, but lives inside the class's namespace for logical organization.
 # Here is a clean code example structured similarly to the image:


class Math:
    @staticmethod
    def add(a, b):
        return a + b

    result = Math.add(1, 2)
    print(result) # Output: 3


'''Static methods Python me aise methods hote hain jo class ke instance ke bajaye directly class se belong karte hain. Inhe @staticmethod decorator ka use karke define kiya jata hai aur inke paas class ke instance (yaani self) ka access nahi hota hai. Inhe class ke instance par nahi, balki directly class par hi call kiya jata hai. Static methods ka use aksar aise utility functions banane ke liye kiya jata hai jinhe instance data ki zaroorat nahi hoti.'''