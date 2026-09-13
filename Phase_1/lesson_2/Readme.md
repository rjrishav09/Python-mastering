
# Lesson 2

In this lesson 2, we will focus on a lot of things post lesson 1.

In this section, python would do the actual decision making.

### 1.Operators

An operator performs an operation on one or more values.

For example:
```python
a = 10
b = 5

print(a + b)
```

Here:
```python
a + b
│   │
│   └── operand
└────── operand

+ → operator
```

So:
```
10 + 5
```
is an expression.

### 2. Arithmetic Operators

Python provides:
```
+     Addition
-     Subtraction
*     Multiplication
/     Division
//    Floor division
%     Modulo
**    Exponentiation
```

#### Addition
```
a = 10
b = 3
print(a + b)
```
Output:
```
13
```
#### Subtraction
```
print(a - b)
```
Output:
```
7
```

##### Multiplication
```
print(a * b)
```
Output:
```
30
```


#### Division
```
print(a / b)
```

Output:
```
3.3333333333333335
```

Important
In Python:
```
10 / 3
```
produces a float.
```
print(type(10 / 3))
```
→
```python
<class 'float'>
```

### 3. Floor Division
```python
print(10 // 3)
```
Output:
```
3
```

It performs division and takes the floor of the result.
```
10 / 3  → 3.333...
10 // 3 → 3
```
We'll revisit negative numbers later because floor division has a subtle behavior worth understanding.

### 4. Modulo(%)

```python
print(10 % 3)
```
Output:
```
1
```

Because:
```
10 = 3 × 3 + 1
```
So % gives the remainder.

This is extremely useful for:
```python
number % 2 == 0
```
which can determine whether a number is even.

Example:
```python
number = 10
print(number % 2 == 0)
```
Output:
```
True
```

### 5. Exponentiation
```python
print(2 ** 3)
```

Output:
```
8
```

Because:
```
2³ = 8
```

### 6. Assignment Operators

We have been already been using:
```
x = 10
```

= means:
Assign/bind this value to this name.
It does not mean mathematical equality.

This is important.
```
x = 10
```
means:
```
bind x to 10
```
It doesn't mean:
```
"x equals 10" in the mathematical sense
```

### 7. Compound Assignment
Instead of:
```python
x = x + 5
```
you can write:
```python
x += 5
```
Similarly:
```python
x -= 5
x *= 5
x /= 5
x //= 5
x %= 5
x **= 5
```
Example:
```python
score = 10
score += 5
print(score)
``` 

Output:
```
15
```

### 8. Comparison Operators
Now we reach something extremely important and which we encouter daily.

```
==     Equal
!=     Not equal
>      Greater than
<      Less than
>=     Greater than or equal
<=     Less than or equal
```

These produce booleans.
```
True
False
```

Example:
```
age = 22
print(age >= 18)
```

Output:
```
True
```
This is the beginning of decision-making.

### 9. == 

Remember:
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
```

Output:
```
True
```
Because their equality comparison says they're equal.

But:
```python
print(a is b)
```
is:
```
False
```
Keep these separate.


### 10. Expressions

An expression is something Python can evaluate to produce a result.

For example:
```
10+5
```
is an expression.

So is:
```python
age >= 18
```

And:
```python
name == "Amritanshu"
temperature > 0.5
```

For example:
```python
age= 22
result = age >= 18
print(result)
```

Output:
```
True
```

### 11. Logical Operators

Now we combine conditions.
Python gives us:
```
and
or
not
```

and: Both Conditions must be true to produce True
```python
age=22
has_started=True
print(age>=18 and has_started)
```

Think:
```
Condition A AND Condition B

True AND True   → True
True AND False  → False
False AND True  → False
False AND False → False
```

### 12. or
Atleast one condition is true.

```python
is_admin = False
is_owner = True

print(is_admin or is_owner)
```

Output:
```
True
```

### 13. not

Reverses Boolean truth.
```python
is_authenticated = True
print(not is_authenticated)
```

Output:
```
False
```

### 14. Conditionals
Now we finally make Python make decisions.

Syntax:
```python
if condition:
    # execute this
```

Example:
```python
age = 22
if age >= 18:
    print("Adult")
```
Output:
```
Adult
```
Notice the colon:
```python
if age >= 18:
```
and indentation:
```python
    print("Adult")
```
Python uses indentation as part of its syntax.


### 15. if + else

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```
Output:
```
Minor
```

Mental model:
```
          age >= 18?
           /      \
         YES       NO
          ↓         ↓
       Adult      Minor
```

### 16. elif
Suppose:
```python
score = 75
```

We can write:
```python
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")
```
Output:
```
B
```

Python checks conditions from top to bottom.
Once it finds a true condition, that branch executes and the remaining elif branches are skipped.

### 17. Truthiness

This is one of the most important Python concepts.
Python doesn't require conditions to literally be:
```
True
False
```

For example:
```python
name = "Amritanshu"
if name:
    print("Name exists")
```
This works.

Why?
Because a non-empty string is considered truthy.

### 18. Falsy Values
Some common falsy values are:
```
False
None
0
0.0
""
[]
{}
set()
()
```

For example:
```python
if "":
    print("True")
else:
    print("False")
```

Output:
```
False
```

```python
if []:
    print("Has items")
else:
    print("Empty list")
```

Output:
```
Empty List
```