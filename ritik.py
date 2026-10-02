def welcome():
    print("Welcome to the program!")

if __name__ == "__main__":
    welcome()


'''In Python, if __name__ == "__main__": acts as a safeguard. It ensures that specific code runs only when the file is executed directly, and not when it is imported as a module into another file.

Here is how Python handles your two files under the hood:

1. __name__ Variable Values
When you run ritik.py directly: Python sets the hidden variable __name__ inside ritik.py to "__main__". The condition __name__ == "__main__" becomes True, so any code inside that block runs.

When you import ritik inside mains.py: Python sets the __name__ variable inside ritik.py to "ritik" (the filename). The condition __name__ == "__main__" becomes False, so the block is skipped.

2. How it works in your project
ritik.py
Python
def welcome():
    print("welcome")

if __name__ == "__main__":
    welcome()
If you run python ritik.py directly: It prints "welcome" because __name__ equals "__main__".

mains.py
Python
import ritik

ritik.welcome()
If you run python mains.py:

import ritik loads ritik.py.

Because it is being imported, ritik.py's __name__ is "ritik", so the if __name__ == "__main__": check fails and welcome() does not run automatically on import.

Then, mains.py explicitly calls ritik.welcome(), printing "welcome".

Note: If you removed if __name__ == "__main__": from ritik.py and kept welcome() at the top level, importing ritik inside mains.py would automatically trigger welcome() right at the import line before you even called it.'''