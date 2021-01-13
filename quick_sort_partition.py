import random
import time


def quick_sort(tar_li, left, right):
    """
    Quick_sort with partition method
    :param tar_li:
    :param left:
    :param right:
    :return:
    """
    a = left
    b = right
    if right - left <= 0:
        return
    val = tar_li[left]
    while left < right:
        while (tar_li[right] > val) and (left < right):
            right -= 1
        if (tar_li[right] <= val) and (left < right):
            tar_li[left] = tar_li[right]
            left += 1
        while (tar_li[left] <= val) and (left < right):
            left += 1
        if (tar_li[left] > val) and (left < right):
            tar_li[right] = tar_li[left]
            right -= 1
    tar_li[left] = val
    print('After partition', tar_li,'\n Start quick sort for left part', tar_li[a:left])
    quick_sort(tar_li,a, left-1)
    print('Start quick sort for right part', tar_li[right+1:b+1])
    quick_sort(tar_li,right+1,b)
    return


tar_li = list(range(10))
random.shuffle(tar_li)
#tar_li = [2,1,5,4,3,2,1]
print(tar_li)
quick_sort(tar_li, 0, (len(tar_li)-1))
print(tar_li)