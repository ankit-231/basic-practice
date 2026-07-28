"""
When a class attribute reference (for class C, say) would yield a class method object, it is transformed into an instance method object whose __self__ attribute is C. When it would yield a staticmethod object, it is transformed into the object wrapped by the static method object. See section Implementing Descriptors for another way in which attributes retrieved from a class may differ from those actually contained in its __dict__.
"""


class Person:

    @classmethod
    def cls_method(cls):
        pass

    @staticmethod
    def stat_method():
        pass

    def normal_method(self):
        pass


"""
We can check out class' attributes with Person.__dict__
"""

print("Person.__dict__", ":", Person.__dict__, end="\n\n")
#  {'__module__': '__main__', 'cls_method': <classmethod(<function Person.cls_method at 0x709ad1718f40>)>, 'stat_method': <staticmethod(<function Person.stat_method at 0x709ad1718fe0>)>, 'normal_method': <function Person.normal_method at 0x709ad1719080>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


"""
For a classmethod, it is transformed into an instance method object whose __self__ attribute is C. So

When doing, Person.cls_method(), python internally sets Person.cls_method.__self__ to Person, and calls it like an instance method (like how a normal method is called, see python_stuff/user_defined_method_obj.py)
"""

p = Person()

print("Person.cls_method.__self__", ":", Person.cls_method.__self__, end="\n\n")

"""
See section Implementing Descriptors for another way in which attributes retrieved from a class may differ from those actually contained in its __dict__
"""

"""
It means accessing the attribute via class (Person.cls_method) and via dict (Person.__dict__["cls_method"]) may result in different values.
"""


print("type(Person.cls_method)", ":", type(Person.cls_method), end="\n")
# type(Person.cls_method) : <class 'method'>

print(
    'type(Person.__dict__["cls_method"])',
    ":",
    type(Person.__dict__["cls_method"]),
    end="\n\n",
)
# type(Person.__dict__["cls_method"]) : <class 'classmethod'>
