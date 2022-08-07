# The generator for powers the input
def PowGen(integer: str, power = 3):
    for number in str(integer):
        yield int(number)**power

def is_armstrong(integer):
    summation = 0
    for powers in PowGen(integer):
        summation += powers
    if summation == integer:
        return True
    return False

print(is_armstrong(153), is_armstrong(370), is_armstrong(371), is_armstrong(407))
print(is_armstrong(200))