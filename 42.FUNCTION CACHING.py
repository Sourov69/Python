# Function caching in Python involves storing the results of expensive function calls and returning the cached result when the same inputs occur again, instead of recomputing the result. This is often achieved using decorators and a data structure, like a dictionary, to store the function's output.

# Importing functools for lru_cache
from functools import lru_cache

# Decorator to cache results
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calculating Fibonacci numbers using the function
print(fibonacci(10))  #
print(fibonacci(8))   #
print(fibonacci(10))  #  

# Another example 
import functools 
import time

@ functools.lru_cache(maxsize = None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")

print(fx(15))
print("Done for 15")
