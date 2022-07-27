from ast import Continue
from decimal import DivisionByZero
from operator import contains
import pickle

def calculate_divides(file_path: str) -> list[float | None]:
    '''Unpickled File & Returned Result Divide Numbers'''
    
    file = open(file_path,"rb")
    numbers = pickle.load(file)
    result = []
    
    while True:
        try:
            
            # I add int() before each item of tuple in order to
            # remove TypeError except statement completely
            # and handle this kind of error automatically
            result = list(map(lambda t: int(t[0]) / int(t[1]), numbers[:2]))
        # TypeError does not need to handle :)
        # except TypeError:
        #    result = [None for _ in numbers]

        # Additionally, I add ZeroDivisionError to check if the denominator is zero.
        # If this error occured, the item remove from list of tuple.
        except ZeroDivisionError:
            continue
        
        finally:
            print(result)
    # file.close()
    # return result


calculate_divides('numbers.pickle')