# Floyd Warshall Algorithm for detecting negative cycle in a weighted directed graph with negative weights.

import typing
import math
import random

INF = math.inf


def buildFWWeightMatrix(mat: typing.List[typing.List[int]]):
    '''
    Problem 1: Floyd-Warshall algorithm implementation
	Computing the shortest-path weights bottom up
	Complexity: O(n^3)
    :param mat: a weight edge matrix
    :return:
    '''
    n = len(mat)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][j], (mat[i][k] + mat[k][j]))


def buildPathMatrix(mat: typing.List[typing.List[int]]) -> typing.List[typing.List[str]]:
    '''
    Problem 2: Constructing the shortest path by Floyd-Warshall algorithm
    Complexity: O(n^3)
    :param mat: a weight edge matrix
    :return: a path matrix
    '''
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j] = 0
    # path matrix initialization:
    pathMat = [[str(i) + "->" + str(j) if mat[i][j] != INF else "" for j in range(n)] for i in range(n)]

    # path matrix building:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k] != INF and mat[k][j] != INF and mat[i][k] + mat[k][j] < mat[i][j]:
                    pathMat[i][j] = pathMat[i][k] + "," + pathMat[k][j]
                mat[i][j] = min(mat[i][j], (mat[i][k] + mat[k][j]))
    return pathMat


def isNegativeCycle(mat: typing.List[typing.List[int]]) -> bool:
    n = len(mat)
    for i in range(n):
        if mat[i][i] < 0:
            return True
    return False

#         (v2)
#          / \\
#       1 /  \\ -5
#        /    \\
#      (v1)---(v3)
#           2
def initInt():
    mat = [[0, 1, INF],
           [INF, 0, -5],
           [2, INF, 0]]
    return mat


def init1():
    mat = [[INF, 3, -10],
           [3, INF, -1],
           [-10, -1, INF]]
    return mat


def init2():
    mat = [[INF, 5, -2],
           [5, INF, -1],
           [-2, -1, INF]]
    return mat


def init3():
    mat = [[0, -1, 10],
           [-1, 0, 2],
           [10, 2, 0]]
    return mat

def init4():
    mat = [[0,INF],
           [-5,0]]
    return mat

def init5():
    mat = [[0,-5],
           [-5,0]]
    return mat

def init6():
    mat = [[INF, 5, 2],
           [5, INF, -1],
           [2, -1, INF]]
    return mat

def init7():
    mat = [[0, 5, 2],
           [5, 0, 1],
           [2, 1, 0]]
    return mat

#   (v1) ---------> (v2)
#    /\\          /
#      \        /
#    2  \     / -10
#        \  |/|
#         (v3)

def init8():
    mat = [[0, 5, INF],
           [INF, 0, -10],
           [2, INF, 0]]
    return mat

def init9():
    mat = [[0, 5, INF],
           [INF, 0, INF],
           [2, -10, 0]]
    return mat

def check_weight_matrices():
    list_matrices = [init1(), init2(), init3(),init4(), init5(), init6(),init7(), init8(), init9()]
    for i in list_matrices:
        checkNegativeCycle(i)
        print()


def printMatrix(mat: typing.List[typing.List[int]]):
    for i in range(len(mat)):
        print(mat[i])


def checkNegativeCycle(mat=initInt()):
    print("Weight matrix before FW:")
    printMatrix(mat)
    # buildFWWeightMatrix(mat)

    path = buildPathMatrix(mat)
    print("Weight matrix after FW:")
    printMatrix(mat)

    print("Is there a negative cycle? ",end="")
    if isNegativeCycle(mat):
        print("Yes")
        print("All paths of a Negative cycle:")
        for i in range(len(mat)):
            if mat[i][i] < 0:
                print("path vertex",i,":", path[i][i])
    else:
        print("No")


if __name__ == '__main__':
    print("Computing whether the graph has negative cycle or not by Floyd-Warshall algorithm:")
    #checkNegativeCycle()
    print()
    check_weight_matrices()
