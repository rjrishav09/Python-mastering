
name="Python"

name[0] = "J"  # This will raise a TypeError since strings are immutable
print(name)  # Output: Python

name="Java"  # This is allowed since we are creating a new string object
print(name)  # Output: Java


a = "Python"
b = a

a = "FastAPI"

print(a)  # FastAPI
print(b)  # Python