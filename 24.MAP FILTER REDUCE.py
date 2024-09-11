# In python map(), filter() and reduce() are built in functions used for
# iteration and data manupulating

# Map function : The map() function in python is used to apply a specific
# function to every item in an iterable (like list) and generates a new 
# iterable with the result
def qube(x):
    return x**3
print(qube(3))
# Generally
l = [1, 2, 3, 4, 5]
newl=[]
for item in l:
    newl.append(qube(item))
print(newl)
# using map it wil verry easy
newl1 = list(map(qube, l))
print(newl1)


# Filter function:
def filter_function(a):
    return a>3
newl3 = list(filter(filter_function, l))
print(newl3)


# Reduce funtion
from functools import reduce
number = [1, 2, 3, 4, 5]
def sum(x, y):
    return x+y
reduce_apply = reduce(sum, number) 
print(reduce_apply)