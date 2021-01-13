import random


def sift(unsorted, low, high):
    largest = low
    left_child = (largest * 2) + 1
    right_child = (largest + 1) * 2
    if (left_child < high) and (unsorted[largest] < unsorted[left_child]):
        largest = left_child

    if (right_child < high) and (unsorted[largest] < unsorted[right_child]):
        largest = right_child

    if largest != low:
        unsorted[largest], unsorted[low] = unsorted[low], unsorted[largest]
        sift(unsorted, largest, high)


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        print('Construct the heap for ', i)
        sift(unsorted, i, n)
    print('Heap done\n',unsorted)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        sift(unsorted, 0, i)
    return unsorted


unsorted = list(range(20))
random.shuffle(unsorted)
print(unsorted)

print(heap_sort(unsorted))