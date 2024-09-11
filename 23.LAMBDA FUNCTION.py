# In python a lambda function is anonymous function created using
# lambda keyword.lambda fucntions are commonly use for simple operation 
# and are particularly handy when you need a function for a short 
# period without defining a full function.They can take any number of arguments 
# But can only have a single expression.

def square(x):
   return x**2

print(square(5))

# when lambda use
multiple = lambda x, y: x*y
print(multiple(5, 4))

qube = lambda z: z**3
print(qube(4))
   
avg = lambda b,c,d:(b+c+d)/3
print(avg(10, 10, 10))

def apply(fx, value):
    return 6 + fx(value)
quv = lambda q: q**3
print(apply(quv, 2))
print(apply(lambda H: H**3, 2))