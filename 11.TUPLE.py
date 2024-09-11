# In Python, tuple is an orderd collection of elemnts, similar to a list
# However , unlike list, tuples are immutable (which mean their contents can not be  changed)
# Tuples are defined using parentheses () and can contain element of diff data types

tup = (1, 2, 3)                   # tup = (i) it will be  a num
Tup = (1, 2, 3, "Red", True)
Tup2 = Tup[1:3]                   # Tup2 = (2, 3)

countries = ("Spain", "Italy", "India", "England", "Germany" )
print(countries)
temp = list(countries)
temp. append( "Bangladesh" )      #add item
temp.pop(3)                       #remove item
temp[2] = "Pakistan"              #change item
countries = tuple(temp)
print(countries)

countries1 = ("Spain", "Italy", "India", "England", "Germany" )
countries2 = ("Bangladesh", "Pakistan")
add = countries1 + countries2
print(add)

