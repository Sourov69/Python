# In python a function is a block reuseable code that performs a specific task or set of tasks.functin are define using def keyword
def function(a, b):
    sum = a + b
    multiplication = a*b
    print(f"sum is {sum}, multiplication is {multiplication}")

function(10, 5)

def isgreater(a=7, b=10):
    if (a>b):
        print('a is greater than b')
    else:
        print("a is smaller than b")

isgreater()

def total(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Total is :", sum/len(numbers)) # sum = sequences elements
total(2, 4, 6, 8)
