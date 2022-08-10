from time import time
from cachetools import cached, TTLCache


cache1 = TTLCache(maxsize=1000, ttl=60)
cache2 = TTLCache(maxsize=1000, ttl=60)

def process_timer(func):
    '''
    decorator for measuring function execuation time
    '''
    turn = 0
    
    def measure(*args, **kwargs):
        nonlocal turn
        turn += 1
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        timer = t2-t1
        return f"The function '{func.__name__}' run in {str(timer)[:8]} sec. This function turn '{turn}' times totally."
    return measure

@process_timer
def fac_without_cache(number):
    '''
    Calculate factorial of an input number.
    '''
    if number == 1:
      return number
    else:
      return fac_without_cache(number-1)*number


@process_timer
@cached(cache1)
def fac_with_cache(number):
    '''
    Calculate factorial of an input number.
    '''
    if number == 1:
      return number
    else:
      return fac_with_cache(number-1)*number

@process_timer
def fib_without_cache(number):
    '''
    Calculate fibonacci series of an input number.
    '''
    if number < 2:
        return 1
    else:
        return fib_without_cache(number-1) + fib_without_cache(number-2)

@process_timer
@cached(cache2)
def fib_with_cache(number):
    '''
    Calculate fibonacci series of an input number.
    '''
    if number < 2:
        return 1
    else:
        return fib_with_cache(number-1) + fib_with_cache(number-2)


print(fac_with_cache(200))
print(fac_without_cache(200))
print(fib_with_cache(20))
print(fib_without_cache(20))


