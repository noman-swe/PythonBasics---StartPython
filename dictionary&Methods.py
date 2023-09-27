dict1 = {}
print(type(dict1))

'''
a = {} #this is how the dictionary is declare
b = set() #this is how the empty set is declare;
print(type(a), type(b))
'''

dict2 = {"Good": "Something pleasant", "Fetch": "To bring", "1": "The Number 1"}
# print(dict2)
print(dict2["Good"])

marks = {"Shibly": "34", "Sadik": "30", "Shanto": "40", "Noman": "20", "Akkas": "17"}
print(marks["Noman"]) # this is how we can be able to retrieve values from keys in dictionary

#we can add in dictionary
marks["Niyon"] = 4

marks.pop("Sadik") #pop needs a argument
print(marks)

print(marks.items())

print(marks.get("Abdullah - Al Noman")) #if the responding value is not available then the result will  be None without showing Error;
print(marks.get("Noman")) #if the responding value is available then the result will be the value of that key; #no error shows in the dictionary.
