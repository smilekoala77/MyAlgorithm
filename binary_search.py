import pytest


def binary_search(li, value):
    high = len(li)-1
    low = 0
    index = lambda high, low: (high + low) // 2
    counter = 0
    while high >= low:
        ind = index(high, low)
        if value == li[ind]:
            print('find the element of ', value, 'and the index is', ind)
            return index
        elif value > li[ind]:
            counter += 1
            print('counter is:', counter, ' target value', value, ' is more than li[{}]='.format(ind), li[ind], \
                  '\nlow is ', low,'high is', high)
            low = ind+1

        elif value < li[ind]:
            counter += 1
            print('counter is:', counter, ' target value', value, ' is less than li[{}]='.format(ind), li[ind], \
                  '\n low is', low, 'high is ', high)
            high = ind-1


lists = list(range(20,50))
binary_search(lists, 18)
