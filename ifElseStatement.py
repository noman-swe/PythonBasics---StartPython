age = int(input("Enter your age : "))

if(age > 18):
    print("Yes, You can vote")
elif(age <= 8):
    print("Hey Kid, What are you doing here?")
else:
    print("No, You can't vote")

print("End of all programs")

# if we put a string value in int(input()) then --: ValueError: invalid literal for int() with base 10: 'shibly' :- this error will be shown