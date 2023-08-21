'''
 * One of version of the gasoline puzzle due to Lovasz.
 * On a very long, circular, isolated driving route there are a number of small
 * gas stations, each with a limited supply of gasoline left.
 * First, check out if in total gas stations contain exactly the amount of gasoline
 * needed to get a car around one full circuit.
 * If it's true, prove that, starting with an empty tank, there is some station
 * we can start at which will allow us to complete one trip around the route.
 * Of course, we will be collecting gasoline whenever we pass a station.
 * Assume a car’s tank is large enough to hold as much as necessary,
 * and that no other cars will be taking any of the available gasoline.
'''
import typing

from Lesson7.best.BestCycle import bestCycle


def petrol_station(a: typing.List[int], b: typing.List[int]) -> bool:
    '''
    the amount of gasoline at the pump in the i gas station: i -> a[i]
    the amount of gasoline needed to get a car a next gas station: i -> b[i]
    sum(b)<=sum(a)
    :param a: the amount of gasoline at the pump in the i gas station: i -> a[i]
    :param b: the amount of gasoline needed to get a car a next gas station: i -> b[i]
    :return: check out if a car can complete one trip around the route or no
    '''
    if len(a) != len(b):
        print("Error: input is nor corrected!")
        return False
    sum_a = 0
    sum_b = 0
    for i in range(len(a)):
        sum_a += a[i]
        sum_b += b[i]
    if sum_b > sum_a:
        print("The total gas stations contain less the amount of gasoline"
              " needed to get a car around one full circuit!!!")
        return False
    c = [(a[i] - b[i]) for i in range(len(a))]
    sum_c = 0
    for i in range(len(c)):
        sum_c += c[i]
    if sum_c < 0:
        print("Not enough gasoline for this driving route!")
        return False
    result = bestCycle(c)
    if result[0] < 0:
        print("Not enough gasoline for this driving route!")
        return False
    print("The details of the contiguous sub interval with the largest sum are:\n"
          "sum_max = {}, interval: [{},{}], length: {}"
          .format(result[0], result[1], result[2], result[3]))
    print("Please start from the station {} (the amount of gasoline is {}) to complete one trip around the route."
          .format(result[1]+1, a[result[1]]))
    return True

def checkPetrolStation(a: typing.List[int], b: typing.List[int]):
    print("\nAmount of gasoline in the gas stations:" + str(a))
    print("Amount of gasoline needed to get a next station:" + str(b))
    print("Can the car complete one trip around the route?", str(petrol_station(a, b)))

def test_correctness():
    list_a = [[3, 6, 2, 8],
              [5, 10, 12, 100],
              [8,10,12,100],
              [6, 0, 0, 6, 7, 0, 7, 8, 5, 5],
              [6,11,13,50]
    ]
    list_b = [[5, 4, 3, 4],
              [6, 11, 13, 50],
              [6,11,13,50],
              [7, 4, 6, 5, 3, 3, 8, 0, 1, 0],
              [8,10,12,100]
        ]
    for i in range(len(list_a)):
        checkPetrolStation(list_a[i], list_b[i])

if __name__ == '__main__':
    # a = [5, 10, 12, 100]
    # b = [6, 11, 13, 50]
    # checkPetrolStation(a,b)
    test_correctness()