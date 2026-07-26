def my_func(first_param: int, default_arg: int = 42) -> str:
    """
    This is a simple function.
    """
    x = 2


def keyword_only_func(*, first_param: int, default_arg: int = 42) -> str:
    """
    This is a simple function.
    """
    return None


"""
# Special read-only attributes
"""

"""
A reference to the dictionary that holds the function’s builtins namespace.

Added in version 3.10.
"""
print("my_func.__builtins__:\n\n", my_func.__builtins__)


"""
A reference to the dictionary that holds the function’s global variables – the global namespace of the module in which the function was defined.
"""
print("my_func.__globals__:\n\n", my_func.__globals__)

"""
None or a tuple of cells that contain bindings for the names specified in the co_freevars attribute of the function’s code object.

A cell object has the attribute cell_contents. This can be used to get the value of the cell, as well as set the value.
"""

print("my_func.__closure__:", my_func.__closure__)

"""
# Special writable attributes
"""
print("my_func.__doc__:", my_func.__doc__)
print("my_func.__name__:", my_func.__name__)
my_func.__name__ = "new_func_name"
print("my_func.__name__ after change:", my_func.__name__)

print("---------------------------------------------------------------------------")

print("my_func.__qualname__:", my_func.__qualname__)
print("my_func.__module__:", my_func.__module__)

"""
A tuple containing default parameter values for those parameters that have defaults, or None if no parameters have a default value.
"""
print("my_func.__defaults__:", my_func.__defaults__)

"""
The code object representing the compiled function body.

compiled bytecode that Python executes. The bytecode could be freshly compiled from the source code, or it could be loaded from a .pyc file. 
"""
print("my_func.__code__:", my_func.__code__)

# you can print the bytecode
print("my_func.__code__.co_code:", my_func.__code__.co_code)

print("---------------------------------------------------------------------------")

"""
The namespace supporting arbitrary function attributes. See also: __dict__ attributes.
"""
# adding custom attributes
my_func.author = "Ankit Khanal"
print("my_func.__dict__:", my_func.__dict__)

print("my_func.__dict__['author']:", my_func.__dict__["author"])
print("above is same as below")
print("my_func.author:", my_func.author)


print("---------------------------------------------------------------------------")
"""
A dictionary containing annotations of parameters. The keys of the dictionary are the parameter names, and 'return' for the return annotation, if provided. See also: object.__annotations__.
"""

# {'first_param': <class 'int'>, 'default_arg': <class 'int'>, 'return': <class 'str'>}
print("my_func.__annotations__:", my_func.__annotations__)

"""
The annotate function for this function, or None if the function has no annotations. See object.__annotate__.

Added in version 3.14.

I am in 3.10, so it results in AttributeError: 'function' object has no attribute '__annotate__'
"""
# print("my_func.__annotate__:", my_func.__annotate__)


"""
function.__kwdefaults__
A dictionary containing defaults for keyword-only parameters.
"""

print("keyword_only_func.__kwdefaults__:", keyword_only_func.__kwdefaults__)

"""
A tuple containing the type parameters of a generic function.

Added in version 3.12.
"""

# print("my_func.__type_params__:", my_func.__type_params__)

print("a".__str__)
print("a".__str__.__str__)
print("a".__str__.__str__.__str__)

"""See infinite_attribute_paradox.py"""
