language = "Python"

print(language[0:3])
# The stop index 3 is excluded.

text = "Python Programming"

print(text[0:6])   # Python
print(text[7:])    # Programming
print(text[7:18])    # Programming
print(text[:6])    # Python
print(text[:])     # Entire string

text = "Python"
print(text[-3:])   # hon
print(text[:-2])   # Pyth

text = "Python"
print(text[::2])   # Pto
print(text[::-1])  # nohtyP
print(text[::-2])  # nhy