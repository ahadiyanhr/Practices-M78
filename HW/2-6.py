# Define a string as input
myString = "www.google.com"

# Define a dictionary for loop
myDict = {}


for element in myString:   # Iterate on each character of string
    
    # Check the character exist in dictionary
    # to avoid duplicate elements
    if element not in myDict:
        
        # Add fresh element and its frequency as key:value
        myDict[element] = myString.count(element)

# Print the result
print(myDict)