# In python, a list is an built-in data structure that can hold a collection of items.
# list are ordered, mutable (meaning can change their contents), and can contain element of different datatypes including numbers, strings, and even other list.
# List are defined using square brackets [] and elements separated by commas(,)

lists = [3, 5, 6, 'sourov', True]
for items in lists:
    print(items)
x = [i for i in range(5)]              #[0, 1, 2, 3, 4]

a = [333, 444, 555, 1, 2, 3, 4, 5, 6]
a.append(7)                            #  a = [333, 444, 555, 1, 2, 3, 4, 5, 6, 7]
a.sort()                               # sequencely orientation a = [1, 2, 3, 4, 5, 6, 333, 444,555]
b = [1, 2, 3, 4, 5]
b.reverse()                            # b = [5, 4, 3, 2, 1]
b.copy()            
c = [333, 444, 555, 1, 2, 3, 4, 6]
c.insert(3, 666)                       # c = [333, 44, 555, 666, 1, 2, 3, 4, 6 ]

p = [1, 2, 3, 4]
q = [3, 4, 10]
p.extend(q)                            # p = [1, 2, 3, 4, 3, 4, 10]


