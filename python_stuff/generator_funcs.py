"""
A function or method which uses the yield statement (see section The yield statement) is called a generator function
"""


# count is a generator function
def count():
    yield 1
    yield 2
    yield 3
    return "abc"


# Such a function, when called, always returns an iterator object which can be used to execute the body of the function
g = count()


# <generator object count at 0x73d67f3b6ff0>
print(g)


# calling the iterator’s iterator.__next__() method will cause the function to execute until it provides a value using the yield statement.
print(g.__next__())  # 1
# above is same as: next(g)

# it resumes execution from where it left off
print(next(g))  # 2

print(next(g))  # 3

# since there are no more yield statements, the next call raises StopIteration
try:
    print(next(g))
except StopIteration as e:

    print("StopIteration raised")
    print("Generator returned:", e.value)


def count_b():
    yield 1
    yield 2
    yield 3
    return "abc"


# we can use while loop instead of manual
b = count_b()
try:
    while True:
        next(b)
except StopIteration as e:
    print("StopIteration from count_b raised")
    print("Generator from count_b returned:", e.value)

# Below would result in an infinite loop since we are creating a new generator object each time in the while loop
# try:
#     while True:
#         next(count_b())
# except StopIteration as e:
#     print("StopIteration from count_b raised")
#     print("Generator from count_b returned:", e.value)
