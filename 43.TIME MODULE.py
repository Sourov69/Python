# The Time module in pyhon provides functionalities to work with time-related tasks, includding time manipulation, conversions.

import time
# Get current time in seconds since the epoch
current_time = time.time()
print("Current time in seconds since the epoch: ", current_time )

# convert  seconds since epoch to a time tuple
time_tuple = time.gmtime(current_time)
print("Time tuple :", time_tuple)

# Format the time into readable string 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print("Formatted time :", formatted_time)

# pause the program for w3 seconds 
print("Waiting for 2 seconds....")
time.sleep(2)
print("2 seocons have passed. ")


print("-----------------------------------------------------------")
# Another example example
import time
def usingwhile():
    i = 0
    while i<500:
        i = i + 1
        print(i)
def usingfor():
    for i in range(500):
        print(i)

init = time.time()
usingfor()
t1 = time.time()-init
init = time.time()
usingwhile()
print(time.time() - init)
print(t1)
# Sleeping time
print(4)
time.sleep(3)
print("This is printed after 3 seconds")
# local time
t = time.localtime()
formatted_time = time.strftime("%y-%m-%D %H:%M:%S", t)
print(formatted_time)