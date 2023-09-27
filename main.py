# my frist python program
print("Hello World")
print("Hello Shibly")

# comment for single line comment (ctrl+/)
''' 
this is multi-line comments:
 print("Hello Shibly")
 print("Hello Shibly")
 print("Hello Shibly")
'''

# variables in Python
a = 3
print('This is a integer', a)
b = 57
print(b)

#this is float in python
a = 5.5
print(a)

#these are the boolean variables
c = True
print(True)
print("c type : ",type(c))
d = False
print(d)

# String in python
e = "Shibly";
print(e)

'''#None is commonly use in Python to represent the absence of a value.'''
f = None
print(f)

'''Typecasting'''
# Typecasting in python (ek data type theke onno data type e conversion)
g = "5"
print(g)
h = 5
print(h)
'''both are showing same value but g is a string and h is a integer datatype variable; this is why we can not able to add any integer value with g,
if we try then there will be a TypeError;'''
# print(g + 2)
'''to solve this error we need to use int(variable);'''
print(int(g) + h)

#multi variable decleration

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

t = {'aaf' : 'fff', 'af' : 'xxx'}
print(type(t))

#another
p = q = r = "Orange"
print(p)
print(q)
print(r)