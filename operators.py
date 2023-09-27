num1 = 10
num2 = 3

'''# Operators'''

# Arithmetic Operators
print("num1 + num2 is :", num1 + num2)
print("num1 - num2 is :", num1 - num2)
print("num1 * num2 is :", num1 * num2)
print("num1 / num2 is :", num1 / num2)
print("num1 // num2 is :", num1 // num2) # //if there is a floating result when you divide then this double forwardSlash will not show you the floating results
print("num1 ** num2 is :", num1 ** num2) #this double ** calculates num1 to the power num2
print("num1 % num2 is :", num1 % num2) #results will be the rest value after divide


# Assignment Operators
print("Assignment Operators")

a = 4
print("just '=' operator :",a)
a += 2
print("with '+=' operator :",a) #plus 2 (a+2)
a -= 2
print("with '-=' operator :", a) #minus by 2 (a-2)
a *= 2
print("with '*=' operator :",a) #multiply by 2 (a*2)
a /= 2
print("with '/=' operator :",a) #divide by 2 (a/2)

b = 4
b **= 2
print("b **= 2 : ",b) # result is : b to the power 2 (b squire)
c = 7
c //= 2
print("c //= 2 : ",c) #shows no floating result after divide
b %= 2
print("b %= 2 : ", b) #shows vagShes which is 0 now


#Comparision Operator
'''
==	Equal, 
!=   Not equal,  
>	Greater than,   
<	Less than,  
>=	Greater than or equal to, 
<=	Less than or equal to
'''

# Logical Operators
'''
' and ' Logical AND: True if both the operands are true
' or '	Logical OR: True if either of the operands is true
' not '	Logical NOT: True if operand is false
'''

print("LOGICAL OPERATOR--")
u = 5
v = 8
w = 5

print(u==w and v>w);
print(u==w and v<w);
print(u==w or v<w);
print(not(False)) #not is used in python to use logic
print(not(True))



# #################################
'''Casting : If you want to specify the data type of a variable, this can be done with casting. '''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


p = 5
q = "John"
# print(type(p))
# print(type(q))