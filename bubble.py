def bubble_sort(array):
    length = len(array) - 1
    for i in range(length):
        for j in range(length-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
