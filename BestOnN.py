'''
 * The maximum subarray problem:
 * finding the contiguous subarray within a one-dimensional array of numbers
 * which has the largest sum.
 * Optimal Best solution
 * Complexity: O(n)
'''
import typing


# Complexity: O(N)
def best(a: typing.List[int]) -> typing.Tuple[int]:
    n = len(a)
    sum_max, begin_max, end_max, length = a[0], 0, 0, 0
    # check if all numbers in a[] are negative
    i = 0
    while i < n and a[i] <= 0:
        i += 1
    # extreme case: all numbers in a[] are negative
    if i == n:
        for j in range(1, n):
            if a[j] > a[begin_max]:
                begin_max = j
        end_max = begin_max
        length = 1
        sum_max = a[begin_max]
    else:
        sum_max = a[i]
        begin_max = i
        end_max = i
        length = 1
        temp_sum, count = 0, 0
        while i < n:
            temp_sum += a[i]
            count += 1
            if temp_sum < 0:
                temp_sum = 0
                count = 0
            elif temp_sum > sum_max:
                sum_max = temp_sum
                end_max = i
                length = count
            i += 1
        begin_max = end_max + 1 - length
    # print(f"{a} sum_max =", sum_max, ", interval: [", begin_max, ",", end_max, "], length =", length, end="")
    return sum_max, begin_max, end_max, length


def test_correctness():
    # arr1 = [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3]  # sum=53
    # arr2 = [3, -2, 5, 1]  # sum=7
    # arr3 = createList()
    # list_arrays = [arr1, arr2, arr3]

    list_arrays = [[5, 100, -150, 5, 20, 100],  # sum_max = 125, interval: [3,5], length: 3
                   [1, 10, -15, 3, -10],  # sum_max = 11, interval: [0,1], length: 2
                   [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3],  # sum_max = 53, interval: [5,6], length: 2
                   [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3, 88],  # sum_max = 94, interval: [8,11], length: 4
                   [10, 2, -5, 8, -100, 3, 150, -180, 1, 2, 3, 88],  # sum_max = 153, interval: [5,6], length: 2
                   [90, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3],  # sum_max = 95, interval: [0,3], length: 4
                   [90, 2, -5, -100, -3, 500, -800, 1, 2, 3, 120],  # sum_max = 500, interval: [5,5], length: 1
                   [90, 2, -5, -100, -3, 500, -800, 100, 200, 30, 120],  # sum_max = 500, interval: [5,5], length: 1
                   [-2, -8, -1, -5, -2],  # sum_max = -1, interval: [2,2], length: 1
                   [2, 8, 1, 5, 2],  # sum_max = 18, interval: [0,4], length: 5

                   [1, 2, 3, -50, 2, 4, -34, 4],  # sum_max = 6, interval: [0,2], length: 3
                   [1, 2, 3, -50, 2, 4, -34, 6],  # sum_max = 6, interval: [0,2], length: 3
                   [3, 3, -50, 1, 2, 3, -34, 4],  # sum_max = 6, interval: [0,1], length: 2
                   [1, 2, 2, 1, -50, 2, 4, -34, 1, 2, 3],  # sum_max = 6, interval: [0,3], length: 4

                   [-1, -2, -2, -1, -50],  # sum_max = -1, interval: [0,0], length: 1
                   [6, -50, 1, 2, 3, -34, 3, 3],  # sum_max = 6, interval: [0,0], length: 1

                   [1, 1, -2, 3, 1, 4, 2, 4, -3, -4, 3, -1, 2, 0, 2, 3, 2, 0, 3, -2],
                   # sum_max = 21, interval: [0,18], length: 19

                   ]

    for i in list_arrays:
        print('\nfor', i)
        print("sum_max = {}, interval: [{},{}], length: {}"
              .format(best(i)[0], best(i)[1], best(i)[2], best(i)[3]))


import random


def createList(size=10):
    lst = [random.randint(-size, size) for i in
           range(0, size)]  # [int(random.random()*(size)) for i in range(-size, size)]
    return lst


if __name__ == '__main__':
    test_correctness()
