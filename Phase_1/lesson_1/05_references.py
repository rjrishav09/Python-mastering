x = 10
y = x

print(x)
print(y)

print(id(x))
print(id(y))


a=[1, 3, 5]
b=a

print(a)
print(b)

b.append(7)
print(a, id(a))
print(b, id(b))
