
## Python Strings
Strings are among the most frequently used data types in Python. In AI engineering, you'll use them to process user queries, prepare prompts, extract information from documents, handle model outputs, and construct API messages.

### Part A - Understanding strings
A string is a sequence of Unicode characters enclosed in quotation marks.

```python
name = "Amritanshu"
language = 'Python'

print(name)
print(language)
```

Both single and double quotation marks work. Use whichever makes your code easier to read.
You can also include quotes inside a string by choosing the other kind of quote:
```python
message = "I'm learning Python"
quote = 'She said, "Hello!"'

print(message)
print(quote)
```

Output:
```
I'm learning Python
She said, "Hello!"
```
For strings that need both types of quotation marks, you can escape a quote with a backslash:
```python
message = "I'm learning \"Python\""
print(message)
```
Output:
```
I'm learning "Python"
```

#### Multiline strings

Triple quotes allow you to create strings spanning multiple lines.
prompt = """You are a helpful AI assistant.
Answer the user's question clearly.
Use examples when appropriate."""
print(prompt)

This is useful when writing longer prompts, although in larger applications we'll also learn to keep prompts in separate files or templates.


### Part B - String indexing
Python strings are ordered sequences. Every character has an index, and indexing starts at 0.

Consider:
```python
language = "Python"
```
##### Positive and negative indexes
The same characters can be accessed from either end of the string.

Positive indexing
P: 0
y: 1
t: 2
h: 3
o: 4
n: 5

Negative Indexing:
P: -6
y: -5
t: -4
h: -3
o: -2
n: -1

Examples:
```python
language = "Python"

print(language[0])   # P
print(language[1])   # y
print(language[5])   # n

print(language[-1])  # n
print(language[-2])  # o
print(language[-6])  # P
```

Positive indexes count from the beginning. Negative indexes count backward from the end, with -1 referring to the last character.

Important: An index outside the string's valid range raises an IndexError.
```python
language = "Python"
print(language[6])  # IndexError
```

The valid positive indexes are 0 through 5, and the valid negative indexes are -6 through -1.

### Part C - String slicing
Indexing retrieves one character. Slicing retrieves a portion of the string.

The syntax is:
```python
string[start:stop:step]
```
a) start: index where the slice begins (included).
b) stop: index where the slice ends (excluded).
c) step: how many positions to move each time.

```python
language = "Python"
print(language[0:3])
```

Output:
```
Pyt
```
The slice starts at index 0 and stops before index 3.

Common slicing patterns
```python
text = "Python Programming"

print(text[0:6])   # Python
print(text[7:])    # Programming
print(text[:6])    # Python
print(text[:])     # Entire string
```

You can also use negative indexes:
```python
text = "Python"
print(text[-3:])   # hon
print(text[:-2])   # Pyth
```

And specify a step:
```python
text = "Python"
print(text[::2])   # Pto
print(text[::-1])  # nohtyP
```

[::-1] is a common Python idiom for reversing a string.

Note:
```
Engineering note

Slicing is particularly useful when you need to extract text from a known position or format. But for real document processing, don't assume important information always appears at fixed character indexes. Use appropriate parsing or text-processing methods when the format varies.
```

### Part D - String immutability
Strings are immutable. Once a string object has been created, you cannot change its characters in place.

For example:
```python
name = "Python"

name[0] = "J"  # TypeError
```

Instead, create a new string:
```python
name = "Python"
name = "J" + name[1:]

print(name)
```

Output:
```
Jython
```

The original string object wasn't modified. The name name was rebound to a new string object.
This is a good place to connect today's topic to your earlier lessons:
```python
a = "Python"
b = a

a = "FastAPI"

print(a)  # FastAPI
print(b)  # Python
```
Unlike our earlier list example, rebinding a does not change what b refers to.


### Part E — Essential string methods

Python provides many built-in string methods. These methods return results you can use in your programs.

1. lower() and upper()

```python
text = "Python Programming"

print(text.lower())
print(text.upper())
```
Output:
```
python programming
PYTHON PROGRAMMING
```
These are useful when comparing text without considering capitalization.
```python
user_answer = "YES"
if user_answer.lower() == "yes":
    print("Confirmed")
```

2. strip(), lstrip() and rstrip()
These remove whitespace from the beginning and/or end of a string.

```python
text = "   Hello Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

Output:
```
Hello Python
Hello Python   
   Hello Python
```

This is particularly useful when processing user input, where accidental spaces can cause unexpected comparisons.

```python
email = input("Enter your email: ").strip()
```

3. replace()

Replace one substring with another:
```python
text = "I am learning Java"
updated_text = text.replace("Java", "Python")
print(updated_text)
```
Output:
```
I am learning Python
```

By default, replace() replaces all matching occurrences.
```python
text = "AI is useful. AI is interesting."
print(text.replace("AI", "Python"))
```

Output:
```
Python is useful. Python is interesting.
```