# In this program we will prove that binary search is quicker way to search a number in an array
# We need to sort the array before using binary search

import random
import time

def naive_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# for binary search the array should be sorted
def binary_search(arr, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr)-1
    if high < low:
        return -1
    
    midpoint = (high + low) // 2

    if arr[midpoint] == target:
        return midpoint
    elif arr[midpoint] < target:
        binary_search(arr, target, midpoint+1, high)
    else:
        # arr[midpoint] > target:
        binary_search(arr, target, low, midpoint-1)

if __name__=='__main__':

    # target = 7
    length = 1000

    sorted_list = set() # we assign it as a 'set' so there will be no repeated value in the list
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()

    print(f"Naive search time is {end - start} seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()

    print(f"Binary search time is {end - start} seconds")