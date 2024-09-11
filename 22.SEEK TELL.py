
with open('file.txt', 'r') as f:
    print(type(f))
    f.seek( 10)              # Move to th 10th byte in the file
    print(f.tell( ) )
# print(".
    data = f.read(5)       # Read the next byteprint(data)

with open('file2.txt', 'r') as x:
    x.write("hello world" )
    x.truncate(4)       # Truncate mean protom theke 4 caracter porjonto |
    print(x)
with open('file2.txt', 'r') as x:
    print(f.read( ) )