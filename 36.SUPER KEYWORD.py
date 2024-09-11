# In python, Super() keyword is used to call a method from a parent or base.
#the super() keyword is used to access methods and properties of a parent class from within a derived class. It's often employed in inheritance to invoke the superclass's methods.

class father:
    def father_method(self):
        print("father says :Its our Car my son")

class son(father):
    def son_method(self):
        super().father_method()

obj = son()
obj.son_method()

# Another example 

class ParentClass:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name from ParentClass: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Calls the parent class constructor
        self.age = age

    def show_info(self):
        super().show_name()  # Accesses the method from the ParentClass
        print(f"Age from ChildClass: {self.age}")

# Create an instance of the ChildClass
child_obj = ChildClass("Sourov", 20)
child_obj.show_info()