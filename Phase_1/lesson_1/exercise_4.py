
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True
print(a is b)  # Output: False

c = a
print(c is a)  # Output: True

"""
Predict the results before running the code.
Then explain why the results differ.

The predicted results are as follows:
print(a == b)  # Output: True
print(a is b)  # Output: False
print(c is a)  # Output: True

== refers to the equality of the values of the objects, while is refers to the identity of the objects in memory.
"""