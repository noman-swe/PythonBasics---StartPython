name = "Noman is a engineer"
number = '5'
print(name)

'''Methods in Python'''
#  slice
print(name[0:3])  # slicing 3 letters
print(name[1:4])  # slicing index 1 to index 3 letters

#  String Methods
print(name.upper())  # makes everything uppercase
print(name.capitalize())  # makes 1st character capitalize
print(name.count(
    "n"))  # has to give an argument; and counts the argument(parameter) value; how much time the argument(parameter) value has in the string;
print(name.isalnum())

print(number.isnumeric())  # tells the string is numeric or not and gives result in boolean
print(name.isnumeric())  # tells the string is numeric or not and gives result in boolean

'''Slicing String'''
#  print the First character
zem = "Hello"[0]
print(zem)

#  Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#  Get the characters from position 2, and all the way to the end:
print(b[2:])

# The strip() method removes any whitespace from the beginning or the end:
print(b.strip())  # returns "Hello, World!"

#  The replace() method replaces a string with another string:
print(b.replace("H", "J"))

#  The split() method splits the string into substrings if it finds instances of the separator
print(b.split(","))  # returns ['Hello', ' World!']
