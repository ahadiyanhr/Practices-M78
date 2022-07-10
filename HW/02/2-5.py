# tupList is a list of non-empty tuples
tupList = [(2,5), (1,2), (4,4), (2,3), (2,1)]

# Define a dictionary and a list
myDict = {}
sortList = []

# for loop for convert input list to dictionary
# keys = second element of each tuple in list
# values = first element of each tuple in list
for i in tupList:
    myDict[i[1]] = i[0]

# Create a sorted list of dictionary keys
sortItems = sorted(myDict)

# Call each key:value from dictionary based on sorted list
for i in sortItems:
    sortList.append((myDict[i], i))
    
# Print the result
print(sortList)

