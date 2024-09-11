# In Python, inheritance is a fundamentalobject-oriented programming concept.It allows you to create a new class that inherits properties (attributes andmethods) from an existing class. The existing class is called the "parent" or"base" class, and the new class isreferred to as the "child" or "derived"class.
#The child class can access and extend the functionality of the parent class.
#To create an inheritance relationship inPython, you define the child class by specifying the parent class inside parentheses when defining the childclass. Here's a basic example


# # # Single Inheritance: A child class inherits from only one parentclass.
class Animal:                    # Parent class
    def __init__(self, species):
        self.species = species
    def make_sound(self):
        pass

class Dog(Animal):              # child class
    def make_sound(self):
        print("Woof")

dog = Dog("Canine")             # Instances of the child classes
print(dog.species)
dog.make_sound()


# # # Multiple Inheritance: A child class inherits from more than one parent class, acquring attributes and methods from all parent classes
class Employee:                            # parent class (1)
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:                              # parent class (2)
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class Dancer_Employee(Employee, Dancer):   # child class from parent(1 + 2)
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

obj = Dancer_Employee("Disco", "Michael Jackson")
print(obj.name)
print(obj.dance)
obj.show()
print(Dancer_Employee.mro())


# # Multilevel Inheritance : In this type of inheritance, a class (subclass) inherits properties and behaviors from a superclass and then becomes a superclass for another class. It forms a chain of classes where each class inherits from its immediate parent, passing on attributes and methods down the chain
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_deatails(self):
        print(f"Name : {self.name} species : {self.species}")
class Dog(Animal) :
    def __init__(self, name, bread):
        Animal.__init__(self, name, species = "Dog" )
        self.bread = bread
    def show_deatails(self):
        Animal.show_deatails(self)
        print(f"species is {self.species}")
class Cat(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, bread = "Haddi")
        self.color = color
    def show_details(self):
        Dog.show_deatails(self)
        print(f"colour is :{self.color}")

obj = Cat("Biral", "white")
print(obj.name)
print(obj.show_deatails())


# # # Hierarchical Inheritance: In Python, hierarchical inheritance refers to a scenario where multiple derived classes inherit from a single base class. Here's an example:

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_car_info(self):
        self.display_info()
        print(f"Fuel type: {self.fuel_type}")


class Truck(Vehicle):
    def __init__(self, brand, model, max_load):
        super().__init__(brand, model)
        self.max_load = max_load

    def display_truck_info(self):
        self.display_info()
        print(f"Max Load: {self.max_load}")


# Motorcycle class also inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, category):
        super().__init__(brand, model)
        self.category = category

    def display_motorcycle_info(self):
        self.display_info()
        print(f"Category: {self.category}")


car = Car("Toyota", "Corolla", "Petrol")
truck = Truck("Volvo", "VNL", "5000 kg")
motorcycle = Motorcycle("Honda", "CBR", "Sport")

car.display_car_info()
truck.display_truck_info()
motorcycle.display_motorcycle_info


# # # Hybrid inheritance occurs when a combination of inheritance types (like multiple and multilevel inheritance) is present in a programming structure. This can happen through a variety of inheritance chains. 

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def display_fuel_type(self):
        print(f"Fuel type: {self.fuel_type}")


class Car(Vehicle, Engine):
    def __init__(self, brand, model, fuel_type, color):
        Vehicle.__init__(self, brand, model)
        Engine.__init__(self, fuel_type)
        self.color = color

    def display_car_info(self):
        self.display_info()
        self.display_fuel_type()
        print(f"Color: {self.color}")


car = Car("Toyota", "Corolla", "Petrol", "Red")
car.display_car_info()
