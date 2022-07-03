#------- Solution 1:
# First, define a function for multiply two numbers
def numMult(x1, x2): 
    return x1*x2
# Second, define a function for calculate the multiplication of a number list
def MultFun(myFunc, list):
    first = list[0]
    for numbers in list[1:]:
        first = myFunc(first, numbers)
    return first

# Finally, print the result
print('Solution 1: ', MultFun(numMult, [8,2,3,-1,7]))

#------- Solution 2:
# We can use reduce() function for this purpose
# First, import reduce() func. from functools
from functools import reduce

# Second, apply reduce() on list with numMult func.
print('Solution 2: ', reduce(numMult, [8,2,3,-1,7]))