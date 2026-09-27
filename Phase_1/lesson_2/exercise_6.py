"""
Exercise 6 — Membership

Create:
skills = ["Python", "FastAPI", "LangChain", "LangGraph"]

Check:
"Python" in skills
"Java" in skills
"LangGraph" in skills
"Java" not in skills

Then create:

agent_state = {
    "messages": [],
    "documents": [],
    "answer": None
}

Check whether these keys exist:

"messages"
"answer"
"tools"
"""

skills = ["Python", "FastAPI", "LangChain", "LangGraph"]

print("Python" in skills)
print("Java" in skills)
print("LangGraph" in skills)
print("Java" not in skills)


agent_state = {
    "messages": [],
    "documents": [],
    "answer": None
}

print("messages" in agent_state)
print("answer" in agent_state)
print("tools" in agent_state)