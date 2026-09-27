"""
Exercise 3 — Logical Operators

Create:
age = 22
has_experience = True
knows_python = True

Write conditions for:
Is the person an adult?
Does the person have both experience and Python knowledge?
Does the person have experience OR Python knowledge?
Does the person NOT know Python?
"""

age = 22
has_experience = True
knows_python = True

if age>=18:
    print("The person is an adult.")

if has_experience and knows_python:
    print("The person has both experience and Python knowledge.")

if has_experience or knows_python:
    print("The person has experience or Python knowledge.")

if not knows_python:
    print("The person does not know Python.")