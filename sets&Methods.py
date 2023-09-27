setsA = {2, 3, 4, 6, 3, 2, 1}
setsB = {52, 90, 100, 3}
print(setsA) # output is : {1, 2, 3, 4, 6} where the double digits are gone and it comes a serial


print(setsA.pop())  #pops a random element and return the poped element
print(setsA)

setsA.add(10) #add in set
print(setsA)

setsA.remove(4)
print(setsA)

print(setsA.intersection(setsB)) #shows the common elements between two sets

print(setsA.union(setsB)) #adds or unions two sets

setsA.clear() #clears the set
print(setsA)

'''Set doesn't repeat it's elements'''
