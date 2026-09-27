"""
Exercise 7 — Agent Simulation 🔥
This one is important.

Create:
documents = [
    "Python basics",
    "FastAPI documentation",
    "LangGraph concepts"
]

Then write a program that:

Checks whether documents contains anything.
If yes, prints "Documents found".
Loops through every document.
Prints each document.
If "LangGraph concepts" exists, prints:
"Agentic AI material found"
Otherwise prints:
"No agentic AI material found"
"""

documents = [
    "Python basics",
    "FastAPI documentation",
    "LangGraph concepts"
]

if documents:
    print("Documents found")

for document in documents:
    print(document)

if "LangGraph concepts" in documents:
    print("Agentic AI material found")
else:
    print("No agentic AI material found")
    



