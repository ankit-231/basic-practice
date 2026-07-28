"""
A class instance is created by calling a class object (see above). A class instance has a namespace implemented as a dictionary which is the first place in which attribute references are searched. When an attribute is not found there, and the instance’s class has an attribute by that name, the search continues with the class attributes. If a class attribute is found that is a user-defined function object, it is transformed into an instance method object whose __self__ attribute is the instance. Static method and class method objects are also transformed; see above under “Classes”. See section Implementing Descriptors for another way in which attributes of a class retrieved via its instances may differ from the objects actually stored in the class’s __dict__. If no class attribute is found, and the object’s class has a __getattr__() method, that is called to satisfy the lookup.

Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary. If the class has a __setattr__() or __delattr__() method, this is called instead of updating the instance dictionary directly.
"""


class Person:

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def stat_method():
        pass

    def norm_method(self):
        pass


p = Person()

"""
p has a namespace implemented with a dictionary type and stored in variable p.__dict__
"""

print("p.__dict__", ":", p.__dict__)  # {}

"""
If I try to access p.norm_method, it will first search p.__dict__, if it does not find it there, it searches Person.__dict__, and since norm_method is a instance method, norm_method.__self__ will be set to p, and Person.norm_method(p) (equivalent) will be called.
"""
