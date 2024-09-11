# The walrus operator, represented by ':=', is used for assignment expressions in Python. It assigns values to variables as part of a larger expression. It allows you to assign a value to a variable as well as use that value in an expression at the same time.


# Without walrus operator
value = 10
if value > 5:
    print(f"The value {value} is greater than 5.")

# With walrus operator
if (value := 10) > 5:
    print(f"The value {value} is greater than 5.")


# Another examples
Happy = False
print(Happy)
# print(Happy=False) # <-------- This is give error
print(Happy := True)# <------ Using (:) it will run cz (:) is wlrus formula
numbers = [1,2,3,4,5]
while(n := len(numbers)) > 0:
    print(numbers.pop( ))
foods = list()
while True:
    food =input("What food do you like?" )
    if food=="quit":
        break
    foods.append(food)
# But when use walrus
Foods = list()
while(Food := input("What song really do you like? :")) !="quit":
    Foods.append(Food)
