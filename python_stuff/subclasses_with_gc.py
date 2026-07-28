import gc


class A:
    pass


"""
Since class B only exists as a local class in create_class function. `A` holds a weak reference to the local subclass B.

Now after create_class() is called, we collect garbage. Python is free to delete B cause it no longer is referenced after create_class() has been called. So, the last A.__subclasses__() prints empty list.

If A.__subclasses__() were to store a strong reference to B, garbage collector would never delete B. In a production scenario, that'd mean every subclasses ever created would never be garbage collected and it would always take up memory leading to memory leaks.
 
"""


def create_class():
    class B(A):
        pass

    print(A.__subclasses__())  # [<class '__main__.create_class.<locals>.B'>]


create_class()

gc.collect()

print(A.__subclasses__())
