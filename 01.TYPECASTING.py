# In python typecasting is the process of converting one data type into another datatype.
# typecasting functions are....

# int()  # float() # str()  # ord()
# list() # tuple()  # set()  # dict()
# hex()  # oct()

# Anything want to know..... print(type(Anything))
a = '1'
b = '2'
print(a+b)                        # output = 12  
print(int(a)+ int(b))             # output = 3
c = 'sourov'
d = '-sir'
print(c+d)                        # output = sourov-sir

# Explcit Typecasting
string = '15'
number = 7
sum = print(int(string)+number)   # output = 22

# implicit typecasting
c = 1.9
d = 8
print(c+d)                        # output = 9.9


# using set() function to remove reapeted value
x = [1, 2, 3, 3, 3, 4, 2, 2, 5, 6, 7, 3, 8,8]
y = set(x)
print(y)

# Using list() function method to convert a set list
l = list(y)
print(l)

# using tuple() function to convert list to tuple
T = tuple(l)
print(T)
