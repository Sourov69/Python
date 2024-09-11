# readlines
f = open('readfile.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break


f = open('read.txt', 'r')
i = 0
while True:
    i +=1
    line = f.readline()
    if not line:
        break
    m1 = line.split(", ")[0]
    m2 = line.split(", ")[1]
    m3 = line.split(", ")[2]
    print(f"marks of student {i} in math is :{m1}")
    print(f"marks of student {i} in english is :{m2}")
    print(f"marks of student {i} in ict is :{m3}")
   
# writeline
y = open('readfile.txt', 'w')
lines = ['!!!!!!!! i am write by sourov!!!!!']
f.writelines(lines)
print(lines)

