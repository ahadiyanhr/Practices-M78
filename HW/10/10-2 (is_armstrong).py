def PowGenFun(integer: str, power: int = 3):
    '''
    A generator function for powers the input number
    '''
    for number in str(integer):
        yield int(number)**power

class PowGencls:
    '''
    A generator class for powers the input number
    '''
    def __init__(self, integer: str, power: int = 3):
        self.integer = str(integer)
        self.power = power
        self.n = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == len(self.integer):
            raise StopIteration
        number = int(self.integer[self.n])
        self.n += 1
        return number**self.power
        

for i in PowGencls(154):
    print(i)        


def is_armstrong_by_fun(integer):
    summation = 0
    for powers in PowGenFun(integer):
        summation += powers
    if summation == integer:
        return True
    return False

def is_armstrong_by_cls(integer):
    summation = 0
    for powers in PowGencls(integer):
        summation += powers
    if summation == integer:
        return True
    return False

print(is_armstrong_by_fun(153), is_armstrong_by_fun(370), is_armstrong_by_cls(371), is_armstrong_by_cls(407))
print(is_armstrong_by_fun(200), is_armstrong_by_cls(300))