# Get a number(int) from user
number = int(input("Enter an integer number:> "))

for j in reversed(range(number)): # Outer loop for iterate on each line
    for i in reversed(range(j+1)): # Inner loop to create a declining consecutive numbers
        if i != 0:
            print(i+1, end = " ") # print number with a space to add another one in next step
        elif i == 0:
            print(i+1) # print the last number of a loop and go the next line
            number -= 1