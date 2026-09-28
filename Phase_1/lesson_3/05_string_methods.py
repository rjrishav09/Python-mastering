# String methods

#1. lower() and upper()

text = "Python Programming"
print(text.lower())  # python programming
print(text.upper())  # PYTHON PROGRAMMING

msg="Hello, World!"

print(msg.lower())
print(msg.upper())

# Strip(), lstrip(), rstrip()
text = "  Python Programming   "

print(text.strip())  
print(text.lstrip())
print(text.rstrip())

# replace()
content = "Java is a programming language. Java is popular."
new_content = content.replace("Java", "Python")
print(new_content)  # Python is a programming language. Python is popular.