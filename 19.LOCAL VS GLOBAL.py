# In python, local variables are defined within a specific function and are 
# only accessible within that functions scope.
# Global variable  are defined outside of any function and can be accessed
# Through the entire code

x = 10       # global variable

def my_function( ):
    y=5      # local variale
    print(y)
my_function( )
print(x)
# print(y)# this will cause an error bacause y is a local varible
# is not accessible outside of the function

x = 20
def my_function( ) :
    global x       # for using this if print x out put=4 not 10 (glbl to local)
    x=4
    y=5
    print(y)
my_function( )
print(x)