from time import time
  
  
def process_timer(func):

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func
  
  
@process_timer
def long_time(n):
    for i in range(n):
        for j in range(100000):
            k = i*j
        return k
  

  
print(long_time(5))