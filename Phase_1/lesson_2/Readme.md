
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

