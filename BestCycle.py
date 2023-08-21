'''
 * The maximum subarray problem in the Cycle/Circular array:
 * finding the contiguous subarray within a cycle/circular array of numbers
 * which has the largest sum.
 * Optimal Best solution
 * Complexity: O(n)
'''
import typing


def best(a: typing.List[int]) -> typing.Tuple[int]:
    '''
    * The maximum subarray problem:
    * finding the contiguous subarray within a one-dimensional array of numbers
    * which has the largest sum.
    * Optimal Best solution
    * Complexity: O(n)
    :param a: an one-dimensional array of numbers
    :return: a tuple that is containing 4 elements:
     a max sum of the interval,
     a begin index,
     an end index of sub-array,
	 and a length of sub-interval
    '''
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


def bestCycle(a: typing.List[int]) -> typing.Tuple[int]:
    '''
	 * Max-Sum subinterval of a Cycle/Circular array:
	 * finding the contiguous sub-array within a cycle/circular array of numbers
	 * which has the largest sum.
	 * Minus Best solution: max-sum is max(Best(A), Sum(A) + Best(-A))
	 * Complexity: O(n)
    :param a: a cycle array of numbers
    :return: a tuple that is containing 4 elements:
     a max sum of the interval,
     a begin index,
     an end index of sub-array,
	 and a length of sub-interval
    '''
    ans_best = best(a)
    sum_best = ans_best[0]  # max-sum of a sub-interval in the source array
    if sum_best < 0:
        return ans_best[0], ans_best[1], ans_best[2], ans_best[3]

    T_arr = []  # an opposite array for the source array
    sum_arr = 0  # sum of all elements in the source array
    n = len(a)
    for i in range(n):
        sum_arr += a[i]
        T_arr.append(-a[i])

    ans_t_best = best(T_arr)
    sum_cyclic_best = sum_arr + ans_t_best[0]  # max-sum of a sub-interval in the cycle array

    if sum_best >= sum_cyclic_best:  # max-sum is a Best(A)
        return ans_best[0], ans_best[1], ans_best[2], ans_best[3]
    else:
        return sum_cyclic_best, (ans_t_best[1] + 1) % n, (ans_t_best[2] - 1) % n, n - ans_t_best[3]


def test_correctness():
    # arr1 = [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3]  # sum=53
    # arr2 = [3, -2, 5, 1]  # sum=7
    # arr3 = createList()
    # list_arrays = [arr1, arr2, arr3]

    list_arrays = [[2, 0, -5, 2],  # sum_max = 4, interval: [3,1], length: 3
                   [-2, 0, 5, -2],  # sum_max = 5, interval: [2,2], length: 1
                   [1, 10, -15, 3, -10],  # sum_max = 11, interval: [0,1], length: 2
                   [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3],  # sum_max = 53, interval: [5,6], length: 2
                   [10, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3, 88],  # sum_max = 109, interval: [5,6], length: 8
                   [10, 2, -5, 8, -100, 3, 150, -180, 1, 2, 3, 88],  # sum_max = 162, interval: [8,6], length: 11
                   [90, 2, -5, 8, -100, 3, 50, -80, 1, 2, 3],  # sum_max = 101, interval: [5,6], length: 7
                   [95, 100, -150, 5, 20, 100]  # sum_max = 320, interval: [3,1], length: 5
                   ]

    for i in list_arrays:
        print('\nfor', i)
        print("sum_max = {}, interval: [{},{}], length: {}"
              .format(bestCycle(i)[0], bestCycle(i)[1], bestCycle(i)[2], bestCycle(i)[3]))


import random


def createList(size=10):
    lst = [random.randint(-size, size) for i in
           range(0, size)]  # [int(random.random()*(size)) for i in range(-size, size)]
    return lst


if __name__ == '__main__':
    test_correctness()
