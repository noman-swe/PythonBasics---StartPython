l1 = [3, 5, 234, 325, 548, 'Abdullah', 234, 4, 7]
print(type(l1))
print(l1)

l1.remove('Abdullah') #removes the 'Abdullah' string from l1 list
print(l1)
l1.count('2')
print(l1.count(234)) #counts the arguments, how much time it is in the list

nickName = ['Shibly', 'Noman', 'Rayan', 420]
print(nickName)

# list.sort() - for sorting we need to remove string from the list
l2 = [3, 5, 234, 325, 548, 234, 4, 7]
print(l2)
l2.sort() #sorts the numbers in accending seial
print(l2)

#list.pop() removes the last element from the list as like array
l1.pop()
print(l1)

#list.append() - adds data which is set as argument in the append() function
l1.append(1000)
print(l1)

#list.extend()
l1.extend([10, 20, 30])
print(l1)

#list.index() - tells the index of the given argument, which is in the list
l1.index(4)
print(l1.index(4))

#list.clear() - clears the full list
nickName.clear()
print(nickName)

'''Notes:
    List is editable 
'''

# editable like --but in tuples we can not do the same
l1[0] = 'Shut up'
print(l1)