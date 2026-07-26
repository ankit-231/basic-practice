"""
The built-in function ord() converts a code point from its string form to an integer in the range 0 to 0x10FFFF; chr() converts an integer in the range 0 to 0x10FFFF to the corresponding length 1 string object. str.encode() can be used to convert a str to bytes using the given text encoding, and bytes.decode() can be used to achieve the opposite.
"""

a = "a"

ord_a = ord(a)  # Output: 97 - The Unicode code point for 'a'.
print(ord_a)

chr_a = chr(ord_a)  # Output: 'a' - Convert the code point back to the character.
print(chr_a)

b = 98
chr_b = chr(b)  # Output: 'b' - The character represented by the Unicode code point 98.
print(chr_b)
