# In python, the enumerate function is a built -in function that is used 
# iterate over elements of an iterable(such as list, tuple, or string)
# while keeping track of the index of the current element 

maks = [12, 56, 98, 12, 45, 1, 4]
idex = 0
for mak in maks:
    print(f"intex {idex} get mark :{mak}")
    idex += 1

# while use enumerate func
marks = [12, 56, 98, 12, 45, 1, 4]
for index, mark in enumerate(marks):
    print(f"serial {index} get {mark} number")
    if mark== 1:
        print("This is last..")

