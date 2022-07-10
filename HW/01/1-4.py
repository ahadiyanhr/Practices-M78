# Get a number from user
Number = input("Enter an integer number:> ") 

''' Solution 1: Reverse the input using Lists '''
NumList = list(Number)  # Convert input number to a list
Rev_Num = [0] * len(NumList) # Create a zero list with the same dimension to input list
Rev1 = ""   # Create an empty string

i = -1
for item in NumList:    # for loop to create a reverse list
    Rev_Num[i] = item
    i -= 1
for item in Rev_Num:    # for loop to convert list to string (Furthermore, I can use {Rev1 = ''.join(Rev_Num)} for the same result)
    Rev1 += item

print("Result of solution 1:", (Rev1))

''' Solution 2: Reverse the input using Strings '''
Rev2 = ""  # Create an empty string
j = -1
for letter in range(len(Number)):
    Rev2 = Rev2 + Number[j]
    j -= 1
    
print("Result of solution 2:", (Rev2))