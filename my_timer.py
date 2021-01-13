import time


def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('%s running time is: %s secs.' % (func.__name__, end_time - start_time))
        return res
    return wrapper

