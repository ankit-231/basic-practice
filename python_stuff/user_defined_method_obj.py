"""
User-defined method objects may be created when getting an attribute of a class (perhaps via an instance of that class), if that attribute is a user-defined function object or a classmethod object.
"""


class Person:

    def greet(self):
        print("Hello Human!")

    @classmethod
    def greet_class(cls):
        print("Hello from the class!")


# Python may create a user-defined method object when we access the greet method through an instance of the Person class.

p = Person()


# This is like a function object
print(Person.greet)

# This will create a user-defined method object for the greet method. It will bind the instance p to the self parameter of the greet method.
print(p.greet)
# Python automatically binds self to the instance
# p.greet() is internally similar to:
Person.greet(p)

# Similarly, Person.greet_class is a class method object. It binds the class Person to the cls parameter.
print(Person.greet_class)

print(p.greet_class)


# Refers to the class instance object to which the method is bound
print(p.greet_class.__self__)

# The new method’s __func__ attribute is the original function object.
print(p.greet.__func__)

"""
When an instance method object is called, the underlying function (__func__) is called, inserting the class instance (__self__) in front of the argument list. For instance, when C is a class which contains a definition for a function f(), and x is an instance of C, calling x.f(1) is equivalent to calling C.f(x, 1).
"""
