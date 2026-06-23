"""
https://docs.python.org/3/reference/datamodel.html#sequences

If start is missing or None, slicing behaves as if start was zero. If stop is missing or None, slicing behaves as if stop was equal to the length of the sequence.

"""

s1 = ["Sam", "John", "Peter", "David", "Michael"]

print(s1[1:4])  # ['John', 'Peter', 'David']


print(s1[1:])  # ['John', 'Peter', 'David', 'Michael']
# above is same as
print(s1[1:None])  # ['John', 'Peter', 'David', 'Michael']

"""
Note that no error is raised if a slice position is less than zero or larger than the length of the sequence.
"""
print(s1[-10:10])  # ['Sam', 'John', 'Peter', 'David', 'Michael']

"""
Some sequences, including built-in sequences, interpret negative subscripts by adding the sequence length. For example, a[-2] equals a[n-2], the second to last item of sequence a with length n.
"""
print(s1[-2:])  # ['David', 'Michael']
