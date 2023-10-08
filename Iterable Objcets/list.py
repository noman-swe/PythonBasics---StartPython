# Declare a list ---
# #List items are indexed, ordered, changeable, and allow duplicate values
# list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Since lists are indexed, lists can have items with the same value:
myFriends = ["Alif", "Shagor", "Sayem", "Sadid", "Sayem", "Mizan", "Shagor"]
myTicketNums = [5464, 5448, 2359, 98, 7842, 602]
myDetails = list(("Shibly", "Swe", 130, "01688126772"))
# print(type(myDetails))
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
######################################################################################################################
# if we add a item then the item will be in the last index

# list.len() - finds the length of the list
totalFriend = len(myFriends)
# print(totalFriend)

# we can get every list item separately by indicating or calling their index no
# print(myFriends[3])

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
# print(mySecondLastFriend)

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
# myFriends[2] = "changeIndex3"
# print(myFriends)

# Changing values in more indexes at a time - index 1 to index 4
# myFriends[1:5] = ["Robo1", "Robo2", "Robo3", "Robo4"]
# print(myFriends)
#myFriends[6:] = ["Rony"]
#print(myFriends)
###########################################################################################
# adding exta value or a less value but difined to change 2 values then the exta values will place beside of the specefic value serially
# Extraaaa value addition
#print(len(myFriends)) # output: 7
myFriends[2:3] = ["Tipu", "Hridoy", "Anik"]
print(myFriends) # added 3 but command to chanage 2 thats why length of the list has increased.
print(len(myFriends)) # output: 9

# adding a less value
myFriends[2:6] = ["Srk", "Msd"] # given index command is to change index (2, 3, 4, 5)= 4 indexes but new values has given for 2, and for this the extra indexes will be removed and the list length will go shorter..
print(myFriends)
print(len(myFriends))
##############################################################################################
'''List Methods'''
# insert() --
# useOfInsert = myFriends.insert("Shihab")
# print(useOfInsert)
