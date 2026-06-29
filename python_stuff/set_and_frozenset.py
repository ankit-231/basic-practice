s1 = set([1, 2])

s1.add(3)

print(s1)


frozenset1 = frozenset([1, 2])
print(frozenset1)
frozenset1.add(3)  # This will raise an AttributeError since frozensets are immutable.
