import pytest
import random

target_array = list(range(100))
#random.shuffle(target_array)
print('target_array is',target_array)

def liner(target_array, value):
    index = 0
    for index, val in enumerate(target_array):
        if target_array[index] == value:
            print('array[{}] is target number'.format(index), val)
            return index
    else:
        print('no target number', value, 'in this array')
        return None


@pytest.mark.parametrize('value,index', [(1, 1), (10, 10), (77, 77), (391, None)])
def test_liner(value, index):
    res = liner(target_array, value)
    assert res == index

