# In Pyhton, Decorator is a powerful and flexiable way to modify or enchance the behavior of functions or method without changing their source code.
# Decorator are often used for tasks such as logging, access control, 
# memoization, etc.Decorator are typically applied to other functions or method using "@" symbol followed by the decorator func name 

def my_decorator(func):
    def dec():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return dec
@my_decorator
def say_hello():
    print("Hello i am called func")

say_hello()

#--------------------------------------------------------------------- 
def decorator_func(name):
    def mname():
        print("Good morning sir")
        name()
        print("Good night sir")
    return mname
@decorator_func
def say_name():
    print("Sourov")

say_name()

#---------------------------------------------------------------------
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"{func.__name__}with args ={args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(5, 7)