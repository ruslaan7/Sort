import numpy as np


def radix_sort(nums):
    radix = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
        buckets = [list() for _ in range(radix)]
        for i in nums:
            tmp = int((i / placement) % radix)
            buckets[tmp].append(i)
        a = 0
        for b in range( radix ):
            buck = buckets[b]
        for i in buck:
            nums[a] = i
            a += 1
        placement *= radix
    return nums


def str_radix_sort(array):
    max_len = -1
    for string in array: 
        str_len = len(string)
        if str_len > max_len:
            max_len = str_len
    oa = ord('A') - 1
    oz = ord('z') - 1
    n = oz - oa + 2
    buckets = [[] for i in range(0, n)] 
    for position in reversed(range(0, max_len)):
        for string in array:
            index = 0 
            if position < len(string):
                index = ord(string[position]) - oa
            buckets[index].append(string)
        del array[:]
        for bucket in buckets: 
            array.extend(bucket)
            del bucket[:]

    return array


def count_sort_day(arr, n):
    output = [None] * n
    count = np.zeros(31, dtype=int)
    for i in range(0, n):
        count[arr[i].DD - 1] += 1
    for i in range(1, 31):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].DD - 1] - 1] = arr[i]
        count[arr[i].DD - 1] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def count_sort_month(arr, n):
    output = [None] * n
    count = np.zeros(12, dtype=int)
    for i in range(0, n):
        count[arr[i].MM - 1] += 1
    for i in range(1, 12):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].MM - 1] - 1] = arr[i]
        count[arr[i].MM - 1] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def count_sort_year(arr, n):
    output = [None] * n
    count = np.zeros(1000, dtype=int)
    for i in range(0, n):
        count[arr[i].YYYY - 2000] += 1
    for i in range(1, 1000):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].YYYY - 2000] - 1] = arr[i]
        count[arr[i].YYYY - 2000] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def date_radix_sort(array):
    n = len(array)
    count_sort_day(array, n)
    count_sort_month(array, n)
    count_sort_year(array, n)
    return array
