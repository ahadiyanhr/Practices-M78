def no_of_arg(func):
    def wrap_func(*args, **kwargs):
        numbers = len(args)
        if numbers == 1:
            result = func(0, args[0], 1)
        elif numbers == 2:
            result = func(args[0], args[1], 1)
        elif numbers == 3:
            result = func(args[0], args[1], args[2])
        return result
    return wrap_func


@no_of_arg
def range(start: int, end: int = None, step: int = 1):
    i = start
    while i <= end:
        j = i
        i += step
        yield j
        
for i in range(10):
    print(i)
print("------")    
for j in range(2, 10):
    print(j)
print("------")     
for k in range(1, 10, 2):
    print(k)