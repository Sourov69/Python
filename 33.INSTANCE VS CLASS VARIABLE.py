# In Python, instance variables are unique to each instance (object) of a class. They are defined within the methods of a class and are accessed using the `self` keyword. Each object can have different values for these variables.

# On the other hand, class variables are shared among all instances of a class. They are defined within the class but outside of any class methods. Changes to a class variable will affect all instances of that class, as they are associated with the class itself, not with any particular instance. These variables are accessed using the class name or the instance name.


class Employee:
    Company_Name = "Apple"         # class variable
    def __init__(self, name):
        self.name = name           # Instance variable
        self.salary = 5000         # Instance variable

    def show_details(self):
        print(f"The Employee is: {self.name} his company is {self.Company_Name} and he get {self.salary}")
    
emp1 = Employee("Sourov")
emp1.show_details()

# variable changing 
emp2 = Employee("Abir")
emp2.Company_Name = "Google"
emp2.salary = 7000
emp2.show_details()


class Example:
    class_variable = 0                  # Class variable

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

# Using the variables
obj1 = Example(5)
obj2 = Example(10)

print(obj1.instance_variable)    # Output: 5
print(obj2.instance_variable)    # Output: 10

print(Example.class_variable)    # Output: 0
Example.class_variable = 1       # Modifying the class variable

print(obj1.class_variable)       # Output: 1
print(obj2.class_variable)       # Output: 1