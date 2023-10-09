# Declare a list ---
# #List items are indexed, ordered, changeable, and allow duplicate values
# list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Since lists are indexed, lists can have items with the same value:
myFriends = ["Alif", "Shagor", "Sayem", "Sadid", "Sayem", "Mizan", "Shagor"]
myTicketNums = [5464, 5448, 2359, 98, 7842, 602]
myDetails = list(("Shibly", "Swe", 130, "01688126772"))
print(type(myDetails))
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
######################################################################################################################
# if we add a item then the item will be in the last index

# list.len() - finds the length of the list
totalFriend = len(myFriends)
print(totalFriend)

# we can get every list item separately by indicating or calling their index no
print(myFriends[3])

# we can get some items form the list at once by indicating their indexes
friendsFrom2To4 = myFriends[2:5]  # it is indicating from index 2 to index 4 & will not include index 5
zeroTo5thFriends = myFriends[:5]  # it is indicating from index 0 to index 4
lastTwoFriends = myFriends[5:]  # it is indicating from index 5 to  the last index
'''print(friendsFrom2To4)
print(zeroTo5thFriends)
print(lastTwoFriends)'''
#####################################################################################
# negative index no indicates indexes from the end
myLastFriend = myFriends[-1]
mySecondLastFriend = myFriends[-2]
print(mySecondLastFriend)

######################################################################################

# check if specific item Exists in the list
# in
if "Mizan" in myFriends:
    print("Yes, He is there.")  # Mizan jodi ei-khaan e thake taile eita print koiro
else:
    print("No, he is not")
# ############# not in
if "Mizan" not in myFriends:
    print("Yes, He is there.")  # mizan jodi ei-khan e thake taile eita print koiro na.
else:
    print("No, he is not")

###########################################################################################
# Changing value in a or some specific value

# Changing values in a value - changing value in no 3 index
myFriends[2] = "changeIndex3"
print(myFriends)

# Changing values in more indexes at a time - index 1 to index 4
myFriends[1:5] = ["Robo1", "Robo2", "Robo3", "Robo4"]
print(myFriends)
myFriends[6:] = ["Rony"]
print(myFriends)
###########################################################################################
# adding exta value or a less value but difined to change 2 values then the exta values will place beside of the specefic value serially
# Extraaaa value addition
print(len(myFriends)) # output: 7
myFriends[2:3] = ["Tipu", "Hridoy", "Anik"]
print(myFriends) # added 3 but command to chanage 2 thats why length of the list has increased.
print(myFriends)
print(len(myFriends))
##############################################################################################
'''List Methods (additions of list items)'''

                    #######################--Insert()--###########################
# insert() -- can add new value but has to specify index no and a new value in the argument
# mainly index declare kore value/list-items add kora jay
myFriends.insert(5,"Shihab")   # 5th index e silo Mizan but Shihab k add koray Mizan 6th index e chole gesy
#print(myFriends)

                    #######################--append()--###########################
# append() -- also adds value in the list but can not specify the index no
myFriends.append("Anik")  # anik k last e add kora hoisy
#print(myFriends)

#######################`````````````````````Deletions````````````````````````###########################

                    #######################--remove()--###########################
# remove - removes specific items given as argument value
myFriends.remove("Sayem")  # sayem removed which was placed before the sadid but after the sadid position's sayem is still there. because, remove() method removes value/list-items but if there is two or more items are in same value then the first indexed of that list-item will be removed.
#print(myFriends)

                        #######################--pop()--###########################
# pop() - removes list-item calling index and just pop() removes from the last
myStr = ["one", "two", "three", 4, "Five", "6"]
print(myStr)
myStr.pop() # removes the last items from the list
print(myStr)

# removes the spefic item from the list calling index no
myStr.pop(3)
print(myStr) # index 3 means value has poped or removed

                        #######################--del keyword--###########################
# del - keyword deletes list items
del myStr[4] # the 4th index data means 5 has deleted
print("Del: ", myStr)

# using del keyword we can delete hole list
del myStr
print(myStr) # myStr List is completely deleted

                        #######################--clear()--###########################
# clear() method clears the list items
myStr.clear()  # this list is empty list now
print(myStr)
#######################````````````````````````Deletions end ``````````````````````##########################

#######################````````````````````````Copy a list ``````````````````````##########################
#copy() -- using this method we can copy a list in a new variable
myEnemy = myFriends.copy()
print(myEnemy)

# list() ei method er maddhon e list copy kora jay
myStudentDetails = list(myDetails)
print(myStudentDetails)
#######################````````````````````````Copy a list ``````````````````````##########################


#######################````````````````````````Joining a list ``````````````````````##########################
# using + (plus) we can join lists
list1 = ["one", "two", "three"]
list2 = [1, 2, 3]
list3 = ["4", "five", 6]
#list4 = list1 + list2 + list3
#print(list4) # three lists has added using +

#extend()
#another way using extend, extend() Add the elements of a list (or any iterable), to the end of the current list
list1.extend(list3)
print(list1)
#extend again
list1.extend(list3 + list2)
print(list1)

#extend() method's another use : converts any iterable-objects(tuples, dict, set) in list
myListItems = ['apple', "kola", "chanachur"]
myTples = (1, 3, 4, 7, 8)
#myListItems.extend(myTples)
print(myListItems)
#######################````````````````````````Joining a list ``````````````````````##########################


#######################````````````````````````Sorting a list ``````````````````````##########################
#list.sort() - Sorts the list; defaultly maintain alphabetically ascending serial
myListItems.sort()
print(myListItems) # alphabetically ascending serial maintain


# -------reverse acending korte chaile sort(reverse = True) likhte hobe;

#-----------
# if the list has case-sensative items then dy default the capitalize case will be placed first and then lower case will be placed
# to place lower case list-item first we have to use listName.sort(key = str.tolower)

#######################````````````````````````Sorting a list ``````````````````````##########################


#######################````````````````````````Sorting a list ``````````````````````##########################
#Loop a list = For Loop
for name in myFriends:
    print("Name :", name)


#while loop
fName = 0
while (fName < len(myFriends)):
    print("Friends name: ", myFriends[fName])
    fName = fName + 1

print("Done List while loop")


# Short form of list for loop
[print("myValuableFriends: ",x) for x in myFriends]

# syntax :newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
''''
details of newlist variable:
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist

# syntax :newlist = [expression for item in iterable if condition == True]

'''
newlist1 = [x if x != "banana" else "orange" for x in fruits]

#######################````````````````````````Sorting a list ``````````````````````##########################


                        #######################--Count--###########################
# count() - method returns the number of elements with the specified value. counts specific value, how much time that specific value are in the list item
useOfCount = myFriends.count("Shagor")
#print(useOfCount)

                        #######################--index()--###########################
# index - returns the index of the first element with the specified value
useOfIndex = myFriends.index("Mizan")
#print(useOfIndex)
#if we have two same list ltem then the first index of that specific item will be printed/taken by using index() method

                        #######################--range()--###########################
#range() - this method returns sequence of numbers, which starts from 0 and increase adding +1;


