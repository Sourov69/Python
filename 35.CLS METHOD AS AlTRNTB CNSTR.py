#A class method used as an alternative constructor is a method within a class that provides an alternative way to create instances of that class, often accepting different parameters or performing additional operations. It's typically named something like " from_something " or "alternate_constructor".

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023  # Assuming the current year is 2023
        age = current_year - birth_year
        return cls(name, age)

# Creating a object using the alternative constructor
sourov = Person.from_birth_year("Sourov", 2003)
print(sourov.name)  
print(sourov.age)   

# Another example
class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
string = "Sourov-12000"
obj = Employee.from_string(string)
print(obj.name)
print(obj.salary)