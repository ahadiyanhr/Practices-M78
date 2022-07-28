'''
I mention 7 notes in below to have better and clear code as below!
'''

# from ast import Continue --> *1* This class does not need because we use "continue-keyword" in our loop
# from decimal import DivisionByZero --> *2* This module does not need because the right error for divide by zero is "ZeroDivisionError"
# from operator import contains --> *3* This module is not required
import pickle

def calculate_divides(file_path: str) -> list:
    '''Unpickled File & Returned Result Divide Numbers'''
    
    file = open(file_path,"rb")
    numbers = pickle.load(file)
    result = []
    
    # *4* We add for-loop before to catch item of numbers list
    # in order to handle each item(tuple) of list easily
    for item in numbers:
        try:
            result.append(item[0]/item[1])
        
        # *5* TypeError handle by convert str to int:
        except TypeError:
            print(f"There is a string item in loop {len(result)+1} which convert to integer!")
            result.append(int(item[0])/int(item[1]))
            continue

        # *6* Additionally, I add ZeroDivisionError to check if the denominator is zero.
        # If this error occured, the item does not append to list:
        except ZeroDivisionError:
            print(f"There is a divide by zero in loop {len(result)+1} that ignored by code!")
            continue
        
        # *7* Moreover, I add finally-statement to force the file close at the end of program.
        finally:
            file.close()
    return result


print(calculate_divides('numbers.pickle'))