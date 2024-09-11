# In Python, "dunder" stands for "double underscore" and refers to special methods surrounded by double underscores at the beginning and end of their names (e.g., __init__, __str__, __len__). These methods are also known as "magic methods" or "special methods."

# Magic dunder methods in Python allow classes to emulate built-in behavior and enable customization of how objects behave in certain situations. For instance,  __init__  is used for object initialization, __str__ controls the string representation of an object,  __len__  determines the length of an object, and  __add__  manages addition for objects, among many others.

# These methods are fundamental for operator overloading, making objects act like built-in types, and enabling certain functionalities like iteration, comparison, arithmetic operations, and more in Python classes.


# # # in magic.py
class Employee:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        i = 0
        for i in self.name:
            i += 1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    def __repr__(self):
        return f"The name of the employee si {self.name}  repr"
    
    def __call__(self):
        print("I am good")

from magic import Souorv
e = Souorv("Sourov")
print(e)
e()
