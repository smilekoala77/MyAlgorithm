import random
import time
from my_timer import *


@cal_time
def select_sort(li):
    """
    :param li: Target list
    :return: Sorted List
    """
    for i in range(len(li)):
        j = len(li)-1
        largest = li[i]
        while j > i:
            #print('largest is ',largest)
            if li[j] > largest:
                largest = li[j]
                counter = j
            j -= 1
        li[counter], li[i] = li[i],largest
    return li


li = list(range(1000))
random.shuffle(li)
li1 = li[:]
print(li)
select_sort(li)
print(li1)
s_t = time.time()
li1.sort()
e_t = time.time()
print('running time of sort is ', e_t - s_t)
