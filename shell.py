def shell_sort(array):
    length = len(array)
    increment = len(array) // 2
    while increment > 0:
        for start in range(increment):
            for i in range(start + increment, length, increment):
                current = array[i]
                position = i

                while position >= increment and array[position - increment] > current:
                    array[position] = array[position - increment]
                    position -= increment

                array[position] = current
        increment //= 2
    return array
