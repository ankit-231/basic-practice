"""
Numbers are immutable in python.

If two variables reference the same number, they will have the same identity.
From docs:  after a = 1; b = 1, a and b may or may not refer to the same object with the value one, depending on the implementation. This is because int is an immutable type, so the reference to 1 can be reused.
"""

a = 1
b = 1

# Output: True - Both a and b reference the same immutable object (1).
print(a is b)

c = []
d = []

# Output: False - c and d reference different mutable objects (empty lists).
print(c is d)

e = f = []

# Output: True - e and f reference the same mutable object (empty list).
print(e is f)
