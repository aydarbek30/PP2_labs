import random

print(random.randrange(1, 5))


x = 5   # int
y = 3.2  # float
z = 4j  # complex
print(type(x))
print(type(y))
print(type(z))

x = 4
y = 123123
z = -123123

print(type(x))
print(type(y))
print(type(z))

x = 3.14
y = 2.0
z = -12.34

print(type(x))
print(type(y))
print(type(z))

x = 12e3
y = 32E1
z = -12.3e456

print(type(x))
print(type(y))
print(type(z))

x = 1+2j
y = 3j
z = -4j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.5  # float
z = 4j   # complex

#int v float:
a = float(x)

#float v int:
b = int(y)

#int v complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))