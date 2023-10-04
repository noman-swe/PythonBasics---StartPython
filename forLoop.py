for i in range(5):
#    print(i, " it prints 0 to 4")
    print(i+1, " it prints 0 to 5")


'''For loop k list er sathew use kora jay, suppose amader ekta list asy li name er'''
print("Printing list.......with ForLoop")
li = [5, 50, 500, 5000, "zero", 8.5]
for item in li:
    print(type(item), item ) #it prints all the item in the list

'''For loop k set er sathew use kora jay, suppose amader ekta set asy s name er'''
print("Printing Set.......with ForLoop")
s = {3, 23, 233}
for setItem in s:
    print(setItem)
#set will never maintain oder or serial - it will be in a randomly way

''' Tuples : For loop k tuples er sathew use kora jay, suppose amader ekta tuples asy t name er'''
print("Printing Tuples.......with ForLoop")
t = (4, 6, 8, 10, 4)
for tupleItem in t:
    print(tupleItem)

''' Dictionary : For loop k Dictionary er sathew use kora jay, suppose amader ekta dictionary asy dictMarks name er'''
print("Printing Dictionary.......with ForLoop")
dictMarks = {"Shibly": "34", "Sadik": "30", "Shanto": "40", "Noman": "20", "Akkas": "17"}
for dictItem in dictMarks:
    print(dictItem) #only prints the keys; to print keys and values we need to do in the below system

for dictItemKey, dictItemValue in dictMarks.items():
    print("Name : {0}, Marks : {1}".format(dictItemKey, dictItemValue)) #this is how we need to print a dictionary's key and value.

dictAges = {"Shakil":24, "Pronab": 50, "Rasel": 54, "Tanvir": 60}
for dictKey, dictValues in dictAges.items():
    print("Name : {0}, Age: {1}".format(dictKey, dictValues))


#loop in string
hips = 'i go to school'
for i in hips:
    print(i)