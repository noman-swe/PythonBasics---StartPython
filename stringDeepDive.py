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

zem = "Hello"[0]
print(zem)
