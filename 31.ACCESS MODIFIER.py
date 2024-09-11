# In python access modifiers are not explicitly declared like in some other language, However, conventions are used to indicate the accessibility of method and variables

class student:
    # constructor is defined
    def __init__(self, name, age):
        self.name = name    # public variable
        self.age = age      # public variable
obj = student("Sourov", 21)
print(obj.name)
print(obj.age)


class Employee:
    def __init__(self):
        self.__name = "Private"  # self.__() create private

Obj = Employee()
# print(obj.__name)              # Cannot be access directly
print(Obj._Employee__name)       # Private variable have to execute indirectly
