try:
    age = int(input("Enter Your age : "))
    if age <= 1:
        print("You are a Infant.")
    elif 2 <= age <= 4:
        print("You are a Toddler.")
    elif 5 <= age <= 12:
        print("You are a Child.")
    elif 12 <= age <= 19:
        print("You are a Teenager.")
    elif 20 <= age <= 39:
        print("You are a Adult")
    elif 40 <= age <= 59:
        print("You are a Middle aged Adult")
    else:
        print("You are a Senior Adult")
except:
    print("Please enter your age in number")

####################################################
'''
try except case with error print has given below
'''
try:
    a = float(input("Enter your number : "))
    print(a + 3)
except Exception as err:
    print("Enter a number not a string, Your error :", err)

# try except use hoy -- jokhno e program e error ashar possibility thake taile try except er maddhom e error handle korte hoy