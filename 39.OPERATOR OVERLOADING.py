# Operator overloading in Python refers to the ability to define and redefine the behavior of operators (+, -, *, /, etc.) for user-defined classes. It allows the same operator to have different meanings depending on the operands' types. For instance, you can define how the "+" operator behaves for instances of your custom classes by implementing special methods (e.g., __add__ for addition) within those classes. This enables you to customize the behavior of operators to work with your objects

class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")
    
    # def __add__(self, x):    
    #     return f"({self.i+x.i}) + {self.j+x.j }j + {self.k+x.k}k"
    # Actual vector operator
    def __add__(self, x):
        return vector(self.i+x.i, self.j+x.j, self.k+x.k)


v1 = vector(3, 5, 6)
print(v1)

v2 = vector(2, 4, 2)
print(v2)

print(v1+v2)


# Another Example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: 'Point' and {}".format(type(other)))

# Creating Point objects
point1 = Point(3, 4)
point2 = Point(1, 2)

# Adding two Point objects using the overloaded operator
result = point1 + point2
print("Resulting Point - X:", result.x, "Y:", result.y)