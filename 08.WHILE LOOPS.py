# In python while loop is a control flow system that repetedly execute a blocks of code as long as a specific contdition is true
# for loop is use if range is not given or unknown
x = 0
while(x<4):
    print(x)
    x = x+1
i = 0
while (i<=15):
    i = int(input('Enter the number = '))     # continuously take user input
    print(i)

count = 5
while (count>0):
    print(count)
    count = count-1                          # decreasing order command
else:
    print('I am inside else')

i = 0
while True:
    number = int(input("Enter the number"))
    print(number)
    if not number >0:
        break
