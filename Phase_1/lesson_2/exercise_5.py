"""
Exercise 5 — Truthiness

Predict the output of:

values = [
    0,
    1,
    "",
    "Python",
    [],
    [1],
    None,
    False,
    True
]

for value in values:
    if value:
        print("Truthy:", value)
    else:
        print("Falsy:", value)

Do not just run it. Predict first.
"""

values = [
    0,
    1,
    "",
    "Python",
    [],
    [1],
    None,
    False,
    True
]


for value in values:
    if value:
        print("Truthy:", value)
    else:
        print("Falsy:", value)

"""
Prediction:
Falsy:0,
Truthy:1,
Falsy:"",
Truthy: "Python",
Falsy: [],
Truthy: [1],
Falsy: None,
Falsy: False,
Truthy: True
"""