i = 0
while i < 10:
    print(i)
    i += 1
# print("Program has finished executing...........") # it we keep indentation then this is printing with the loop
print("Program has finished executing...........")  # and this is printing after the loop because of no indentation

'''
while(True):
    print("Infinite Loop") #this loop is a infinite loop
'''
'''
# we can put conditions to remove infiniteness
while(True):
    num = int(input("Enter a number : "))
    print("Your Number is : ", num)
    if(num ==0):
        break # when the input value will be equal to 0 then this infinity loop will be break
'''

'''
z = 0
while z < 7:
    print(z)
    if z == 3:
        break
    z += 1
'''
'''     break and continue
Break: Break is a kind of  stopper
Continue: Continue is kind of skip
'''
# Continue Practice
f = 1
for f in range(5):
    if f == 3:
        continue
    print(f + 1)
# in this case 4 is skipped while printing; because we set when f == 3 then the next will be skipped

# Break Practice
print("Break Practice")
b = 1
for b in range(10):
    if b == 5:
        break
    print(b + 1)
