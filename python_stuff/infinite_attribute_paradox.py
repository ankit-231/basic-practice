"""
So, what I found is that below is valid in python:
print("a".__str__)
print("a".__str__.__str__)
print("a".__str__.__str__.__str__)

It is because the string "a" is an object of class str, so it has __str__ method which itself is an object, so it has __str__ method, and so on. So, it is an infinite chain of __str__ methods.
"""

print("a".__str__)
print("a".__str__.__str__)
print("a".__str__.__str__.__str__)


"""
So, why doesn't python crash there will be infinite chain of __str__ methods?
Python only evaluates what is asked for, so unless I do "a".__str__.__str__.__str__, it's value was never evaluated by python.
"""
