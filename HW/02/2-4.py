def DigiKala(Last):
    First = ''  # First is defined to compare with Last
    
    while First != Last:    # Compare First is equal to Last
        myDict = {}     # a Dictionary for counting the repetition of numbers
        for i in Last:
            if i not in myDict:     # Check the number is unique
                myDict[int(i)] = Last.count(i)  # key: Unique Number, Value: Repetition
        
        # Join the list of Unique Numbers with Repetition > 1:
        myList = list(myDict.keys())+[x for x in myDict.values() if x > 1]
        myList.sort()   # Sort the list in place
        
        # Convert the list items to str and join it together with map():
        strList = ''.join(map(str,myList))
        
        # Replace the new First and Last for next while condition
        First = Last
        Last = strList
        
    return Last
 
# Example:           
NumString = '442254545'
print(DigiKala(NumString))