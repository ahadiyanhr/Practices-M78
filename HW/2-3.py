def checkPrime(_number_):
    for i in range(2, _number_):
        if not int(_number_) % i:
            return False
    return True

print(checkPrime(12))
print(checkPrime(7))