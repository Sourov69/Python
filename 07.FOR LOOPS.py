# In python  a for loops is a control flow statement used for iterating over a sequence(such as list, tuple, string or range) or any iterable obj
# We use for loops when we know the range or we have some sequencial items

name = 'Sourv'
for i in name:
    print(name)                 # s o u r v
    print(name, end=' ')        # ->
    if (i=="r"):
        print('o')              # s o u r o v

colors = ['Red', 'Green']
for color in colors:
    print(color)                # Red Green
    for letter in color:
        print(letter)           # Red R e d  Green G r e e n

for number in range(1, 11):
    print(number)               # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in range(1, 11):
    print(f"5 X {i} = {5*i}")
    if (i==5):
        continue
    elif (i==7):
        break 
