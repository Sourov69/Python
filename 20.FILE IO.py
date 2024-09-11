# File I\O(Input\Output) in python refers to the processes of 
# reading from  and writing to files on my computer
# The fileIO concept incapsulates various operations that allows to
# open(), read(), write(), close(),

 # Reading a file
f = open('fileio20.txt', 'r') #'w', 'a''rb' mean binry te khula
# f = open('myfile.txt2', 'w') # new file open in left side
# print(f)
text = f.read()
print(text)
# f.close()

# Writing a file
f = open('fileio20.txt', 'a') #'w', 'a'f.writel'Hello world!' )
f.close( )

# # Short method
with open('fileio20.txt', 'a') as f:
    f.write("Hey í am inside with" )