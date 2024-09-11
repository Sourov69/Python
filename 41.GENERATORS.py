# Generators in Python are special functions that behave as iterators. They produce a sequence of values using the yield statement instead of return. They enable you to generate a series of values lazily, allowing you to iterate through large or infinite sequences without storing them in memory all at once. This makes them memory efficient and useful for handling large datasets or streams of data.

def number_generator(n):
    for i in range(n):
        yield i

# using the generator
gen = number_generator(5)
# iterating through the generator to retrieve values
for num in gen:
    print(num)


def my_generator():
    for i in range(500):
        yield i

Gen = my_generator()
print(next(Gen))
print(next(Gen))
print(next(Gen))
