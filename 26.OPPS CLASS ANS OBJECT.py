# In Python, a class is a blueprint that defines the attributes and behaviors of objects.
# It serves as a template for creating objects, which are instances of that class.
# Objects are specific instances of a class, possessing their own unique characteristics and data,while following the structure and behavior defined by the class. Essentially, a class is a design or model, while an object is an instance or realization of that model in memory.

class person:
    name = "sourov"           
    age = 20                  
    occupation = "Programmer" 
    
object = person()
print(object.name)
object.name = "Abir"          
print(object.name)


class Animal:
    name = "Dog"
    age = 2
    color = "white"
    def info(self):   # Any func creating in a class must pass
                      # default self argument
        print(f"The {self.color} color {self.name} is {self.age} years old")
                           
obj = Animal()
obj.info()