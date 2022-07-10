# Get a list from user
List = input("Enter a list items separated by space:> ").split()    # Create the input numbers to a list

ModifiedList = []   # Create a modified list without duplicate items

for item in List:   # Iterate on list items
    if item not in ModifiedList:    # Checking items does not exist in modified list
        ModifiedList.append(item)   # Append fresh items to modified list
        
print(ModifiedList)