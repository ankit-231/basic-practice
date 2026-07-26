"""
Modules are a basic organizational unit of Python code, and are created by the import system as invoked either by the import statement, or by calling functions such as importlib.import_module() and built-in __import__().

A module object has a namespace implemented by a dictionary object (this is the dictionary referenced by the __globals__ attribute of functions defined in the module). Attribute references are translated to lookups in this dictionary, e.g., m.x is equivalent to m.__dict__["x"]. A module object does not contain the code object used to initialize the module (since it isn’t needed once the initialization is done).

Attribute assignment updates the module’s namespace dictionary, e.g., m.x = 1 is equivalent to m.__dict__["x"] = 1.
"""

# using import statement
import math

# using importlib.import_module()
import importlib

math_module = importlib.import_module("math")

"""
importlib.import_module gives a ModuleType object.
"""
another_way_to_import_math = __import__("math")

print("math_module.sqrt(9) -->", math_module.sqrt(9))  # Output: 3.0

print(
    "another_way_to_import_math.sqrt(16) -->", another_way_to_import_math.sqrt(16)
)  # Output: 4.0

print("math is math_module -->", math is math_module)  # Output: True
print(
    "math is another_way_to_import_math -->", math is another_way_to_import_math
)  # Output: True

# ===============================================================================


import my_module

print("my_module.x -->", my_module.x)
print("my_module.my_function() -->", my_module.my_function())


# the __dict__ attribute
# print(my_module.__dict__)

# my_module.x is equivalent to my_module.__dict__["x"]
print(
    'my_module.x is my_module.__dict__["x"] -->', my_module.x is my_module.__dict__["x"]
)  # Output: True
print('my_module.__dict__["x"] -->', my_module.__dict__["x"])

"""
A module object does not contain the code object used to initialize the module (since it isn’t needed once the initialization is done)
I don't fully understand this.
"""
# print("my_module.__code__ -->", my_module.__code__)
# Above throws AttributeError
