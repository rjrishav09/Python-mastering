# Information

This file will contain all the respective information about the phase 1.
The focus will be on the "Python" specially Python for AI Engineers.

## Python

#### 1. What is Python?
Python is a high-level, dynamically typed, general-purpose programming language which also supports Object Oriented feature.

Python uses Interpreter to execute the program.

```
Python
 ├── FastAPI              → Backend APIs
 ├── Pydantic             → Data validation
 ├── NumPy                → Numerical computing
 ├── Pandas               → Data processing
 ├── PyTorch              → Deep Learning
 ├── Transformers         → LLMs
 ├── LangChain            → LLM applications
 ├── LangGraph            → Agentic workflows
 └── Databricks           → Data + AI platform
```

####  2. How Does Python Actually Execute Code?

When I execute python app.py, then the Python interpreter takes your source code and executes it through Python's runtime machinery.

A simplified python mental model is:
```
Your Python Code
       ↓
Python Interpreter
       ↓
Python Bytecode
       ↓
Python Runtime / Virtual Machine
       ↓
Result
```

Just remember:
Python source code is executed by the Python runtime. Python isn't simply "compiled directly to machine code" in the same way as traditional compiled languages.
.py -> Python interpreter/runtime -> execution


#### 3. First Python Program

```python
print("Hello, AI Engineering!")
```

#### 4. Variables

```python
name = "Amritanshu"
age = 25
```

In python school of thoughts, variables can be understood as names/ references pointing to the objects.
Or in simple words you can understand it as variables are in stack and pointing to its value in Heap.

Think:
```
name
  │
  ▼
┌──────────────┐
│ "Amritanshu" │
│    object    │
└──────────────┘
```

So, name = "Amritanshu" means approximately:
Create/find the string object "Amritanshu" and bind the name name to it.

#### 5. Python Variables Don't Have Fixed Types

```python
x=10
x="hello"
x=3.14
```
The name x doesn't have a permanent type.
The object has a type.
This is one of the most important ideas in Python.

#### 6. What Does "Dynamically Typed" Mean?

x=10
Python knows: 10-> int

x="Hello"
Python knows: "Hello"-> str

So the type associated with the object can change as the name gets rebound.

Compare that with a statically typed language such as Java:
int x = 10;

You generally can't then do:
x = "hello";

7. type() — Your First Useful Tool

```python
type()
```

#### 8. Python's Fundamental Data Types

For now, the focus will be on the following:
```
| Type       | Example   |
| ---------- | --------- |
| `int`      | `10`      |
| `float`    | `10.5`    |
| `str`      | `"hello"` |
| `bool`     | `True`    |
| `NoneType` | `None`    |
```
Later the focus will be on: list, tuple, set, dict

#### 9. Integers
Python integers can become extremely large.

For example:
number = 999999999999999999999999999999999999999

Python can handle this without the fixed-size integer limitations you may have encountered in languages such as JavaScript.