cow = "The cow is a domestic animal, cow gives us milk. it has a nose"
username = "nomanswe130"
phone = "016881267722"

# slicing a string
slicingUserName = username[0:5]  # it will take index 0 to 4 & will stop taking before 5th index.
slicingDeptName = username[5:8]  # it will take index 5 to 7 & will stop taking before 8th index.
print("Name of the user : ", slicingUserName)
print("Department of the user : ", slicingDeptName)

'''case capitalize(), upper(), lower(), islower() and casefold()'''
# capitalize() - Converts the first character to upper case
capitalUser = username.capitalize()
print(capitalUser)

# upper() - Converts a string into upper case
upperUserName = username.upper()
print(upperUserName)

# lower() - Converts a string into lower case
lowerCase = upperUserName.lower()
print(lowerCase)

# The islower() method returns True if all the characters are in lower case, otherwise False.
checkIsLower = username.islower()
print(checkIsLower)

# casefold() - Converts string into lower case
lowerCaseByCaseFold = cow.casefold()
print(lowerCaseByCaseFold)
'''
noto::
capitalize() - converts to capital-case of a strings first letter.
upper() - converts all the string to uppercase.
lower() - converts all the to lowercase.
casefold() - same as lower case.
islower() - cheeks the hole string is in lowercase & if it is lowercase then return True Otherwise returns False
'''

'''endswith() and startswith() '''
# endswith() - Returns true if the string ends with the specified value
endsWithTest = username.endswith("130")
print(endsWithTest)

# startswith() - Returns true if the string starts with the specified value otherwise False
startsWithTest = username.startswith("no")
print(startsWithTest)
'''endswith() and startswith() '''

'''
            find(), index() || rfind(), rindex()
            
find(), index() :- the both method finds the first occurrence of the specified value.
and rfind(), rindex() :- Those method finds the last occurrence of the specified value.
those can take 3 arguments; 
1.value(required)-The value to search for, 
2.Start(Optional)-Where to start the search. Default is 0, 
3.end(Optional) - Where to end the search. Default is to the end of the string 

'''
# find() and index() - searches the string for a specified value and returns the first occurrence position of where the specified was found
findFirstCow = cow.find("cow")
print(findFirstCow)

findFistAlpha = username.index("n", 4, 10)
print(findFistAlpha)
# rfind() and rindex() - Searches the string for a specified value and returns the last occurrence position of where the specified was found
findLastCow = cow.rindex("cow")
print(findLastCow)

findLast_a = cow.rindex('a')
print(findLast_a)
findLastA = cow.rfind("a", 15, 25)
print(findLastA)
'''
find(), index(), -- both are same; Those method finds the first occurrence of the specified value.

rfind(), rindex() -- both are same; Those method finds the last occurrence of the specified value.
'''

#
'''isalnum(), isalpha(), isnumeric(), isdigit(), isdecimal(), isspace(), '''
# isalnum() - The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(username.isalnum())
# returns True, if the string has both alphabet and numeric value in the string, without any space in that string. syntax= string.isalnum()

# isalpha() - The isalpha() methods returns true if all the characters are alphabet letters (a-z) in the string.
print(cow.isalpha())
print(slicingUserName.isalpha())
# returns True, if the string has only alphabet value in the string,and even without any space in that string. syntax= string.isalpha()

# isnumeric() - The isnumeric() methods returns true if all the characters are numeric value (0-9) in the string otherwise False.
print(phone.isnumeric())  # returns true because the phone variable is full of numeric characters.
print(
    username.isnumeric())  # returns False because the username variable has an alphanumeric value, it requires only numeric value.

# isdecimal() - The isdecimal() method returns True if all the characters are decimals value (0-9) in the string otherwise False.it's totally same to isnumeric()
print("isdecimal: ", phone.isdecimal())
print("isdecimal: ", username.isdecimal())

# isdigit() - The isdigit() method returns True if all the characters are digits, otherwise False.
print(phone.isdigit())  # it's kind of numeric but also takes unicode values and returns True;

# isspace() is returns True only when the string has only whitespace value
whiteSpace = " "
print("Whitespace : ", whiteSpace.isspace())

'''
isalnum(), isalpha(),
isnumeric() & isdecimal(),:: isnumeric() and isdecimal() are totally same;;
isdigit(),  
isspace(), 
'''

'''lstrip(), rstrip() Starts'''

txtTestStrips = "     banana     "

# lstrip() : Remove spaces to the left of the string
lstripTest = txtTestStrips.lstrip()
print("lStrip: Of all fruits", lstripTest, "is my favorite")

# rstrip() : Remove spaces to the right of the string
rstripTest = txtTestStrips.rstrip()
print("rStrip: Of all fruits", rstripTest, "is my favorite")

'''lstrip(), rstrip() End'''

'''#Start# split(), rsplit() :: both are same; both gives same output'''
# The split() and rsplit() method splits a string into a list. starting from the right.
# #Syntax :: string.split(separator, maxsplit)
# #we can specify the separator, default separator is any whitespace.
splitTxt = "apple, banana, cherry"

splitTest = splitTxt.split(",")
print(splitTest)

rsplitTest = splitTxt.rsplit(", ")
print(rsplitTest)

'''#End# split() ,rsplit()::: both are same.'''

'''replace()'''
# replace() - The replace() method replaces a specified phrase with another specified phrase.
# syntax :: string.replace(oldvalue, newvalue, count); here old and new value is required and count is optional
goat = cow.replace("cow", "goat")
print(goat)

# how much time we want to change that word/alphabet in our string we can declare by the count argument
horse = cow.replace("cow", "horse", 1)
print(horse)  # output: The horse is a domestic animal, cow gives us milk. it has a nose;;; because i've set count 1 that's why horse replace cow once and second was cow again..

'''replace()'''
