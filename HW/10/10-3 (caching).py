import os
# from time import process_time_ns
from cachetools import cached, TTLCache


cache1 = TTLCache(maxsize=1000, ttl=60)
cache2 = TTLCache(maxsize=1000, ttl=60)

def exec_times(some_function):
    '''
    decorator for measuring function execuation time
    '''
    t1 = 0
    def times(*args, **kwargs):
        nonlocal t1
        t1 += 1
        some_function(*args, **kwargs)
        return t1
    return times

@exec_times
def fac_without_cache(number):
    '''
    Calculate factorial of an input number.
    '''
    if number == 1:
      return number
    else:
      return fac_without_cache(number-1)*number


@exec_times
@cached(cache1)
def fac_with_cache(number):
    '''
    Calculate factorial of an input number.
    '''
    if number == 1:
      return number
    else:
      return fac_with_cache(number-1)*number

@exec_times
def fib_without_cache(number):
    '''
    Calculate fibonacci series of an input number.
    '''
    if number < 2:
        return 1
    else:
        return fib_without_cache(number-1) + fib_without_cache(number-2)

@exec_times
@cached(cache2)
def fib_with_cache(number):
    '''
    Calculate fibonacci series of an input number.
    '''
    if number < 2:
        return 1
    else:
        return fib_with_cache(number-1) + fib_with_cache(number-2)


# @decorator_timer
# def fac_without_cache(number):
#     fac = factorial(number)
#     return fac

# @decorator_timer
# def fib_without(number):
#     fib = fib_without_cache(number)
#     return fib


# @decorator_timer
# def fac_with_cache(number):
#     fac = factorial(number)
#     return fac


# @decorator_timer
# def fib_with(number):
#     fib = fib_with_cache(number)
#     return fib


# os.system("cls")
# print("Elapsed time during the program in microseconds\nFactorial:", fac_without_cache(1000), end = "\n")
print(fac_with_cache(100))
print(fac_without_cache(100))
print(fib_with_cache(10))
print(fib_without_cache(10))

# print("Fibonacci1:", process_time_ns()-t1)

# print("Elapsed time during the program in microseconds\nFactorial:", fac_with_cache(1000), end = "\n")
# print("Fibonacci:", fib_with_cache(30))


