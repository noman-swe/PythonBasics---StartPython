cow = "The cow is a domestic animaL.The cow gives us milk"

# Converts the first character to upper case
print("capitalize() : ", cow.capitalize())

# makes every chere
print(cow.upper())

# Converts string into lower case
print("casefold(): ", cow.casefold())
print("lower(): ", cow.lower())

# Returns the number of times a specified value occurs in a string
wordCount = cow.count("cow")

# print(wordCount)
print(cow.count("cow"))

# Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
xEndsWith = txt.endswith("world.")
notEndsWith = txt.endswith("Haven")
print(xEndsWith)
print(notEndsWith)

#  find() -returns the specified argument or the value is where or the position index number or can say: Searches the string for a specified value and returns the position of where it was found
practiceFind = cow.find("h")
print(practiceFind)

# index() - returns the specified argument or the value is where or the position index number or can say: Searches the string for a specified value and returns the position of where it was found
practiceIndex = cow.index("cow")
print(practiceIndex)

#  isalnum()  - Returns True if all characters in the string are alphanumeric || works for only alphabet not for hole string
userNameTxt = "nomanswe130"
nickName = "Noman"
alfaNumericTest = userNameTxt.isalnum()
alfaNumericTest_2 = cow.isalnum()
print("alfaNumericTest Username: ", alfaNumericTest)  # true
print("alfaNumericTest Cow: ", alfaNumericTest_2)  # false

#  isalpha() -  Returns True if all characters in the string are in the alphabet || works for only alphabet not for hole string
testIsAlfa = nickName.isalpha()
print(testIsAlfa)

#  isdigit() - Returns True if all characters in the string are digits, but it will not work for decimal
digitsTxt = "232323"
print(digitsTxt.isdigit())

#  isdecimal() - Returns True if all characters in the string are decimals
print("Decimal: ", digitsTxt.isdecimal())

# isnumeric() - Returns True if all characters in the string are numeric
isNumericTest = digitsTxt.isnumeric()
print(isNumericTest)

#  Returns True if all characters in the string are whitespaces
whiteSpace = "   "
print("White space : ", whiteSpace.isspace())

# The lstrip() method removes any leading characters (space is the default leading character to remove)
txtIsTrip = ",,,,,ssaawwpppppx.....banana"
tripedWord = txtIsTrip.lstrip(",.aswpx")
print(tripedWord)

# string.split(separator, maxsplit) - The split() method splits a string into a list. where separator and maxsplit are Optional.