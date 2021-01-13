import random
from my_timer import cal_time
import time


@cal_time
def bubble_sort(li):
    """
    :param li: list that is need to be sorted
    :return: sorted list
    """
    for i in range(len(li)):
        # print('i = ', i)
        j = len(li) - 1
        ex_flag = True
        while j >= i:
            #            print('li[{}]='.format(j), li[j], ' li[{}]='.format(j - 1), li[j - 1])
            if li[j] > li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
                ex_flag = False
                #                print('Exchanged li[{}]'.format(j), ' and li[{}]'.format(j - 1))
                # print(li)
            j = j - 1
        if ex_flag:
            return li
    return li


li = list(range(1000))
random.shuffle(li)
#print(li)
bubble_sort(li)

s_t = time.time()
li.sort()
e_t = time.time()
print('running time of sort is {} secs'.format(e_t - s_t))

