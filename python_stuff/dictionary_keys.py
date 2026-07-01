"""
The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity
"""

di = {1: "one", 2: "two", 3: "three"}
print("di:", di)

# invalid_di = {[1, 2]: "one-two"}  # This will raise a TypeError: unhashable type: 'list'
# print("invalid_di:", invalid_di)

"""
The keys should be of a type that is immutable and hashable. the reason being that the efficient implementation of dictionaries requires a key’s hash value to remain constant.
"""

"""
Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g., 1 and 1.0) then they can be used interchangeably to index the same dictionary entry.
"""
another_di = {1: "one", 1.0: "one point zero"}
print("another_di:", another_di)

yet_another_di = {1: "one"}
print("yet_another_di[1.0]:", yet_another_di[1.0])  # "one"

# Note that 1 == 1.0 is True, even though their identities are different.
print("1 == 1.0:", 1 == 1.0)  # True
print("id(1) == id(1.0):", id(1) == id(1.0))  # False
print("id(1):", id(1), "id(1.0):", id(1.0))  # Different memory addresses
print("hash(1):", hash(1), "hash(1.0):", hash(1.0))  # Same hash values

"""
Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added sequentially over the dictionary. Replacing an existing key does not change the order, however removing a key and re-inserting it will add it to the end instead of keeping its old place.
"""

my_di = {}
my_di["first"] = 1
my_di["second"] = 2
print("my_di after adding keys:", my_di)

# remove first key and re-insert it
del my_di["first"]
my_di["first"] = 1
print("my_di after removing and re-inserting 'first':", my_di)

"""
Changed in version 3.7: Dictionaries did not preserve insertion order in versions of Python before 3.6. In CPython 3.6, insertion order was preserved, but it was considered an implementation detail at that time rather than a language guarantee.
"""
