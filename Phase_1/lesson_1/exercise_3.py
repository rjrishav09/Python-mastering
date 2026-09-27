
a=[1, 2, 3]
b=a

print(a, type(a))
print(b, type(b))

b.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]

print (a is b)  # Output: True
print(id(a))
print(id(b))
"""
Then explain why both changed.

It didn't change because both a and b are referencing the same mutable list object in memory.

"""


