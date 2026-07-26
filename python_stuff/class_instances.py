"""
Instances of arbitrary classes can be made callable by defining a __call__() method in their class.
"""


class MyCallableClass:
    def __call__(self, *args, **kwargs):
        print(f"Calling an instance of {self.__class__.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")


my_callable_instance = MyCallableClass()
# Calling the instance like a function
my_callable_instance(1, 2, key="value")
