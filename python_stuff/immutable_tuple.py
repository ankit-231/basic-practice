# if an immutable container (like a tuple) contains a reference to a mutable object, its value changes if that mutable object is changed.

mutable_object = [3, 4]
tp = (1, 2, mutable_object)

print(tp)  # Output: (1, 2, [3, 4])

mutable_object.append(5)

# Output: (1, 2, [3, 4, 5]) - The tuple itself is immutable, but the mutable object it contains has changed.
print(tp)
