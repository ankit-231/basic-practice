"""
type.__subclasses__()
Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. The list is in definition order. Example:

>>> class A: pass
>>> class B(A): pass
>>> A.__subclasses__()
[<class 'B'>]



"Still alive" refers to classes that have not been garbage collected.
"""


class A:
    pass


class B(A):
    pass


print("A.__subclasses__()", ":", A.__subclasses__())
# >>> A.__subclasses__() : [<class '__main__.B'>]
