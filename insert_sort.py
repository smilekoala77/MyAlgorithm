import random
from my_timer import *


def insert_sort(li):
    """
    :param li: Target list
    :return: Sorted List
    """
    for i in range(len(li) - 1):
        tmp = li[i+1]
        j = i
        while (tmp > li[j]) and (j >= 0):
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        #print(li)

    return li


li = list(range(100))
random.shuffle(li)
print(li)
print(insert_sort(li))
