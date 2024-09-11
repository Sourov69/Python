
a = int(input("Enter your age =" ))
print("Your age is:", a)



# conditional operators
# <,>,<=,>=, ==,!=

if(a>18):
    print("You can Drive" )
else:
    print("You can not Drive")
    print( "Yay!" )

num = int(input("Enter the number="))
if (num < 0):
    print("Number is negetive" )
elif (num > 0):
    if (num <= 10):
        print("Number is between 0-11")
    elif (num > 10 and num <=10):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")