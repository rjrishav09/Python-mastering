""" Assignment Operator and Compound Assignment Operator"""

#This file will demonstrate the use of assignment operators and Compound Assignment operators in Python.

x = 5
print("Initial value of x:", x)
print(type(x))  # Output: <class 'int'>

# Compound Assignment Operators
x+=5
print(type(x)) 
print("Value of x after x+=5:", x)

x-=5
print(type(x)) 
print("Value of x after x-=5:", x)

x*=5
print(type(x)) 
print("Value of x after x*=5:", x)

x/=5
print(type(x)) 
print("Value of x after x/=5:", x)

x**=5
print(type(x)) 
print("Value of x after x**=5:", x)
