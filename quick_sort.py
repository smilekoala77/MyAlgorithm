import random
import time
from my_timer import *


def quick_sort(tar_li):
    """
    Using list to implement quick sort
    :param tar_li: target list
    :return: sorted list
    """
    print('quick sort for', tar_li)
    if len(tar_li) < 2:
        return tar_li
    pivot = tar_li.pop(0)  # using the first element as pivot
    large = []
    less = []
    for element in tar_li:
        (large if element > pivot else less).append(element)
    print('less is: ',less,'middle is: ',pivot, 'large is: ',large)
    return quick_sort(less) + [pivot] + quick_sort(large)


tar_li = list(range(10))
random.shuffle(tar_li)
print(tar_li)
# s_time = time.time()
quick_sort(tar_li)
# e_time = time.time()
# print('Running time of quick_sort is', e_time-s_time)
