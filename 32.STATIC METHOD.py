# In Python, a static method is a method that belongs to a class rather than an instance of the class. Static methods are defined using the " @staticmethod " decorator and do not depend on the state of any specific instance. They are typically used for utility functions that are related to the class but don't need access to instance-specific data.

# 1. They are defined within the class but don't take the self parameteras their first argument, unlikeregular instance methods.
#2 . Static methods can be called on the class itself, without needing to create an instance of the class.

class Myclass:
    @staticmethod
    def static_method(x, y):
        return x + y
# No need to instantiate the class to use the static method
result = Myclass.static_method(10, 5)
print(result)          # output = 50

# Another example
class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self, n):
        self.num = self.num + n
        
    @staticmethod
    def add(a, b):
        return a + b

obj = Math(5)
obj.addtonum(5)
print(obj.num)

stc_method = Math.add(20, 30)
print(stc_method)