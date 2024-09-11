# In, Python Exception handling is a mechanism that allow me to gracefully handle
# errors or exceptions that may occur during the  execution of my code
# The primary constructs for handling exception in python are...
# try, except, finally, rise

a = input("Enter the number: ")
print(f"Multiplication table of {a} is :" )
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}" )
# except Exception as e:
# print(e)
except:
    print("sorry you put invalid number" )
finally:
    print("I will always execute")  


print(" try:use korle majkhane error asleo sheser code run hoy")
print(" try: tarpor code tarpor except:diye end korte hoy, except erjaygay kon tipe error ta lekha jay")print(".
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("index error")

a = int(input("Enter any value between 5 and 9"))

if (a<5 or a>9):
    raise ValueError  "Value is wrong"
        # SyntaxError "Syntax is wrong"
        # MemoryError "Memory loss"



