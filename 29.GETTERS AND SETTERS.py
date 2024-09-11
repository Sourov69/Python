# In Python, getters and setters are methods used to access and modify class attributes.
# Getters are used to access the value of an attribute,
# while setters are used to modify or set the value of an attribute.
# It can be implemented using @property decorators or by defining methods with specific naming conventions (like 'get_attribute and' 'set_attribute').


class MyClass:
    def __init__(self):
        self._value = 0              # Private variable

    @property
    def value(self):
        return self._value           # Getter

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value  # Setter

# Using the class
obj = MyClass()
print(obj.value)      # Accessing the value (getter)

obj.value = 10        # Setting the value (setter)
print(obj.value)      # Accessing the updated value
obj.value = -5        # Trying to set a negative value (setter won't allow it)
print(obj.value)      # The value remains unchanged


### Using Getter and Setter Methods:
class MyClass:
    def __init__(self):
        self._value = 0                     # Private variable

    def get_value(self):
        return self._value                  # Getter

    def set_value(self, new_value):
        if new_value >= 0:
            self._value = new_value         # Setter

    value = property(get_value, set_value)  # Property linking the getter and setter methods

# Using the class
obj = MyClass()
print(obj.value)                            # Accessing the value (getter)

obj.value = 10                              # Setting the value (setter)
print(obj.value)                            # Accessing the updated value
obj.value = -5                              # Trying to set a negative value (setter won't allow it)
print(obj.value)                            # The value remains unchange


