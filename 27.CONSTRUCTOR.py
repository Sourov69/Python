# In python a constructor is special method use to initialize objects of a class.It define using the ( __init__ ) method within the class definiation
# when i create an instance of a class, the constructor is automatically called it allowing me to set up the initial state of the object by specifying its attributes and their initial values.

class Myclass:
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2

# Creating an instances of Myclass and invoking the constructor
my_instance = Myclass("value1", "value2")

class person:
    def __init__(self, n, o):
        print("Hello i am Hacker")
        self.name = n
        self.occupation = o
    def info(self):
        print(f"{self.name} is a {self.occupation}")

p = person("Sourov", "singer")
p.info()


