# slicing in python refers to the technique of extracting a portion of a data  by specifiying a range of indices
name = 'sourov, talukder'
print(len(name))
print(name[8:16])                   # Talukder

letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(letter[0:4])                   # ABCD
print(letter[0:12:2])                # mean interval 2 
print(letter[:-3])                   # mean first to last-3
print(letter[-5:-3])                 # mean (last-5) to (last-3)

tup = (0, 1, 2, 3, 4, 2, 3, 6, 8, 2, 1, 5)
print(tup.index(3)) # mean 6 koto number line e ase?
print(tup.index(3, 4, 8)) #mean 3 number ta 4-8 er modde koto number ase ?