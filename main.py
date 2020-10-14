import numpy as np
import random
from bubble import bubble_sort
from shell import shell_sort
from quick import quick_sort
from merge import merge_sort
from heap import heap_sort
from radix import radix_sort, date_radix_sort, str_radix_sort
from time import perf_counter_ns
import string
from dataclasses import dataclass

ranges = np.array([50000])


@dataclass
class Date:
    YYYY: int
    MM: int
    DD: int

    def __lt__(self, other):
        return (self.YYYY, self.MM, self.DD) < (other.YYYY, other.MM, other.DD)

    def __gt__(self, other):
        return (self.YYYY, self.MM, self.DD) > (other.YYYY, other.MM, other.DD)


def sorting_short_rand():
    print("РАНДОМНЫЕ МАЛЕНЬКИЕ ЧИСЛА")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = i % 10

        random.shuffle(short)

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_int_rand():
    print("РАНДОМНЫЕ ЦЕЛЫЕ ЧИСЛА")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = i

        random.shuffle(short)

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_str_rand():
    print("РАНДОМНЫЕ СТРОКИ")
    for number in ranges:
        short = list()
        for i in range(number):
            short.append(''.join(random.choice(string.ascii_lowercase) for _ in range(np.random.randint(1, 10))))

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        str_radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_date_rand():
    print("РАНДОМНЫЕ ДАТЫ")
    for number in ranges:
        short = list()
        for i in range(number):
            date = Date(YYYY=1000, MM=random.randint(1, 12), DD=random.randint(1, 28))
            short.append(date)

        random.shuffle(short)

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        date_radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_short_semi_rand():
    print("ЧАСТИЧНО УПОРЯДОЧЕННЫЕ МАЛЕНЬКИЕ ЧИСЛА")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = i % 10

        random.shuffle(short[int(len(short) / 5):int(2 * len(short) / 5)])
        random.shuffle(short[int(3 * len(short) / 5):int(4 * len(short) / 5)])

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_int_semi_rand():
    print("ЧАСТИЧНО УПОРЯДОЧЕННЫЕ ЦЕЛЫЕ ЧИСЛА")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = i

        random.shuffle(short[int(len(short) / 5):int(2 * len(short) / 5)])
        random.shuffle(short[int(3 * len(short) / 5):int(4 * len(short) / 5)])

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_str_semi_rand():
    print("ЧАСТИЧНО УПОРЯДОЧЕННЫЕ СТРОКИ")
    for number in ranges:
        short = list()
        for i in range(number):
            short.append(''.join(random.choice(string.ascii_lowercase) for _ in range(np.random.randint(1, 10))))
        short = np.asarray(short)

        short[0:int(len(short) / 5)] = sorted(short[0:int(len(short) / 5)])
        short[int(2 * len(short) / 5):int(3 * len(short) / 5)] = sorted(short[int(2 * len(short) / 5):int(3 * len(short) / 5)])
        short[int(4 * len(short) / 5):int(5 * len(short) / 5)] = sorted(short[int(4 * len(short) / 5):int(5 * len(short) / 5)])

        newshort = list()
        for j in range(len(short)):
            newshort.append(short[j])

        # start = perf_counter_ns()
        # bubble_sort(newshort.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(newshort.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(newshort.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(newshort.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(newshort.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        str_radix_sort(newshort.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(newshort.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_date_semi_rand():
    print("ЧАСТИЧНО УПОРЯДОЧЕННЫЕ ДАТЫ")
    for number in ranges:
        short = list()
        for i in range(number):
            date = Date(YYYY=1000, MM=random.randint(1, 12), DD=random.randint(1, 28))
            short.append(date)

        short = np.asarray(short)

        short[0:int(len(short) / 5)] = sorted(short[0:int(len(short) / 5)])
        short[int(2 * len(short) / 5):int(3 * len(short) / 5)] = sorted(
            short[int(2 * len(short) / 5):int(3 * len(short) / 5)])
        short[int(4 * len(short) / 5):int(5 * len(short) / 5)] = sorted(
            short[int(4 * len(short) / 5):int(5 * len(short) / 5)])

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        date_radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_short_same_rand():
    print("МАССИВ ИЗ ОДИНАКОВЫХ МАЛЕНЬКИХ ЧИСЕЛ")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = 1

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_int_same_rand():
    print("МАССИВ ИЗ ОДИНАКОВЫХ ЦЕЛЫХ ЧИСЕЛ")
    for number in ranges:
        short = np.zeros(number, np.int64)
        for i in range(len(short)):
            short[i] = 654

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_str_same_rand():
    print("СТРОКИ ИЗ ОДИНАКОВЫХ ЭЛЕМЕНТОВ")
    for number in ranges:
        short = list()
        symbol = random.choice(string.ascii_lowercase)

        for i in range(number):
            short.append(''.join(symbol))

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        str_radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


def sorting_date_same_rand():
    print("МАССИВ ИЗ ОДИНАКОВЫХ ДАТ")
    for number in ranges:
        date = Date(YYYY=1000, MM=random.randint(1, 12), DD=random.randint(1, 28))
        short = list()
        for i in range(number):
            short.append(date)

        short = np.asarray(short)

        # start = perf_counter_ns()
        # bubble_sort(short.copy())
        # end = perf_counter_ns()
        # bubble_time = end - start
        # print("Сортировка пузырьком с размером массива: ", number, " Время: ", bubble_time)

        start = perf_counter_ns()
        shell_sort(short.copy())
        end = perf_counter_ns()
        shell_time = end - start
        print("Сортировка Шелла с размером массива: ", number, " Время: ", shell_time)

        start = perf_counter_ns()
        quick_sort(short.copy())
        end = perf_counter_ns()
        quick_time = end - start
        print("Быстрая сортировка с размером массива: ", number, " Время: ", quick_time)

        start = perf_counter_ns()
        merge_sort(short.copy())
        end = perf_counter_ns()
        merge_time = end - start
        print("Сортировка слиянием с размером массива: ", number, " Время: ", merge_time)

        start = perf_counter_ns()
        heap_sort(short.copy())
        end = perf_counter_ns()
        heap_time = end - start
        print("Сортировка кучей с размером массива: ", number, " Время: ", heap_time)

        start = perf_counter_ns()
        date_radix_sort(short.copy())
        end = perf_counter_ns()
        radix_time = end - start
        print("Поразрядная сортировка с размером массива: ", number, " Время: ", radix_time)

        start = perf_counter_ns()
        sorted(short.copy())
        end = perf_counter_ns()
        sorted_time = end - start
        print("Встроенная в язык сортировка с размером массива: ", number, " Время: ", sorted_time)

    return 0


sorting_short_rand()
sorting_int_rand()
sorting_str_rand()
sorting_date_rand()

sorting_short_semi_rand()
sorting_int_semi_rand()
sorting_str_semi_rand()
sorting_date_semi_rand()

sorting_short_same_rand()
sorting_int_same_rand()
sorting_str_same_rand()
sorting_date_same_rand()
