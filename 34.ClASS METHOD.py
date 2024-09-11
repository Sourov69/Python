# In Python, a class method is a method that is bound to the class, not the object instance. It's defined using the " @classmethod " decorator. It takes the class itself as the first argument commonly named cls, rather than the instance of the class (commonly named self in instance methods).

class MyClass:
    class_variable = 10
    
    @classmethod
    def class_method(cls, x):
        cls.class_variable += x
        return cls.class_variable

# Accessing the class method without creating an instance of the class
result = MyClass.class_method(5)
print(result)                    # Output  15

# Accessing the class variable via the class itself
print(MyClass.class_variable)  # Output  15

# Another Exaple
class Employee:
    company_name = "Apple"

    def show(self):
        print(f"The Employee is: {self.name} his company is {self.company_name}")
    
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

emp1 = Employee()
emp1.name = "Sourov"
emp1.show()

emp2 = Employee()
emp2.name = "Abir"
emp2.change_company("Tesla")
emp2.show()    

print(Employee.company_name)  # Output : "Tesla " not "Apple" because @classmethod take the class itself as the first arguments"