"""
Classes are callable. These objects normally act as factories for new instances of themselves, but variations are possible for class types that override __new__(). The arguments of the call are passed to __new__() and, in the typical case, to __init__() to initialize the new instance.


The return value of __new__() should be the new object instance (usually an instance of cls).
"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        print(f"Creating a new instance of {cls.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        # return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(f"Initializing the instance of {self.__class__.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")


# if I remove the return value of __new__() method, it will return None, and __init__() method will not be called.
my_instance = MyClass(1, 2, key="value")

print(my_instance)
