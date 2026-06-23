"""
https://docs.python.org/3/reference/datamodel.html#numbers-integral

These represent the truth values False and True. The two objects representing the values False and True are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings "False" or "True" are returned, respectively.
"""

print(False)
print(True)

# get the identity of the objects
print(id(False))
print(id(True))


# Damn, they really do act like 0 and 1, respectively.
print(False + 1)
print(True + 1)

# string representation
print(str(False) + " is a boolean value, now converted to string.")
print(str(True) + " is a boolean value, now converted to string.")
