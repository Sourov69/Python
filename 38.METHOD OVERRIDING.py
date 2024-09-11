# Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass. This allows the subclass to change the behavior of that method without changing the method's name or signature.

import math 
class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
    
    def area(self):
        return  math.pi * super().area()

rectangle = shape(4, 3)

c = circle(5)
print(c.area())


# Another Example

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating instances and calling the overridden method
generic_animal = Animal()
dog = Dog()
cat = Cat()

generic_animal.sound()  # Output: Generic animal sound
dog.sound()              # Output: Bark
cat.sound()              # Output: Meow