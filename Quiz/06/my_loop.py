
def loop(number: int):
    
    print(f"loop in {number}")
    if (number-1) >= 0:
        return loop(number-1)
    
loop(4)
    