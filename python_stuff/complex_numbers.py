"""
https://docs.python.org/3/reference/datamodel.html#numbers-complex-complex

These represent complex numbers as a pair of machine-level double precision floating-point numbers. The same caveats apply as for floating-point numbers. The real and imaginary parts of a complex number z can be retrieved through the read-only attributes z.real and z.imag.
"""

comp_num = 3 + 4j
print(comp_num)
print(comp_num.real)
print(comp_num.imag)

another_comp_num = complex(5, 6)
print(another_comp_num)
