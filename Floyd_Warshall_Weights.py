# Floyd Warshall Algorithm for finding the shortest path between all the pairs of vertices in a weighted graph.

import typing
import math
import random

# What value will be defined for an infinity number?
# One of assume is define infinity as the large enough value.
INF = 99999
# Another assume to make sure that it is handled the maximum possible value,
# is the value of INF can be taken as a positive infinite integer value,
# for example, from the math module (as math.inf)
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
    print("Path matrix before FW:")
    printMatrix(pathMat)

    # path matrix building:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k] != INF and mat[k][j] != INF and mat[i][k] + mat[k][j] < mat[i][j]:
                    pathMat[i][j] = pathMat[i][k] + "," + pathMat[k][j]
                mat[i][j] = min(mat[i][j], (mat[i][k] + mat[k][j]))
    return pathMat


def connectComponentsOfGraph(mat: typing.List[typing.List[int]]) -> [int, typing.List[typing.List[int]]]:
    '''
    Problem 3: Find a number of connected component
    and get a list of vertices in each connected components
    :param mat: a int matrix
    :return:
    '''
    # first, find a number of connected components
    # in the undirected graph (square symmetric matrix)
    n = len(mat)
    connectComp = [0 for i in range(n)]
    numComponentes = 0
    for i in range(n):
        if connectComp[i] == 0:
            numComponentes += 1
            # connectComp[i] - a component number of the vertex i
            connectComp[i] = numComponentes
        for j in range(i + 1, n):
            # vertex j is not defined yet
            if connectComp[j] == 0 and mat[i][j] != INF:
                # the vertex j was defined and the path between (i,j) exists
                connectComp[j] = numComponentes

    # last, get a vertices list of each connected components
    vertexInComponent = [[] for i in range(numComponentes)]
    for i in range(len(connectComp)):
        index = connectComp[i] - 1
        vertexInComponent[index].append(i)

    # printMatrix(vertexInComponent)
    return numComponentes, vertexInComponent


def isConnected(mat: typing.List[typing.List[int]]) -> bool:
    '''
    Problem 4: Check the connectivity of the graph
    Complexity: O(n^2)
    :param mat: a int matrix
    :return: true if a graph is connected otherwise false
    '''
    n = len(mat)
    ans = True
    for i in range(n):
        if ans:
            for j in range(n):
                if ans:
                    if mat[i][j] == INF:
                        ans = False
    return ans


def isConnectedComplexN(mat: typing.List[typing.List[int]]) -> bool:
    '''
    Problem 4: Check the connectivity of the graph
    Complexity: O(n)
    :param mat: a int matrix
    :return: true if a graph is connected otherwise false
    '''
    n = len(mat)
    ans = True
    for i in range(n):
        if mat[0][i] == INF:
            ans = False
    return ans


#             2
#       (0)------(3)
#       /          \
#  18  /            \ 4
#     /              \
#   (4)             (2)
#     \             /
#      \          /
#    5  \       / 1
#        \    /
#         (3)

def initInt():
    mat = [[0, 2, INF, INF, 18],
           [2, 0, 4, INF, INF],
           [INF, 4, 0, 1, INF],
           [INF, INF, 1, 0, 5],
           [18, INF, INF, 5, 0]]
    return mat


def init1():
    mat = [[1, 9, 6, INF],
           [9, 8, INF, 18],
           [6, INF, 5, 15],
           [INF, 18, 15, 10]]
    return mat


def init2():
    mat = [[1, INF, INF, INF],
           [INF, 1, 1, 1],
           [INF, 1, 1, 1],
           [INF, 1, 1, INF]]
    return mat

def init3():
    mat = [[INF,1,1,INF,INF,INF],
           [INF,INF,1,1,INF,INF],
           [INF,INF,INF,1,INF,INF],
           [1,INF,1,INF,INF,INF],
           [INF,INF,INF,INF,INF,1],
           [INF,INF,1,INF,INF,INF]]
    return mat

def check_weight_matrices():
    list_matrices = [init1(), init2(), init3()]
    for i in list_matrices:
        checkFW(i)
        print()


def checkFW(mat=initInt()):
    print("Check Floyd-Warshall algorithm:")
    print("Weight matrix before FW:")
    printMatrix(mat)
    # buildFWWeightMatrix(mat)
    # print("Weight matrix after FW:")
    # printMatrix(mat)

    path = buildPathMatrix(mat)
    print("Path matrix after FW:")
    printMatrix(path)

    print("Is the graph connected?", isConnected(mat) and isConnectedComplexN(mat))

    # the shortest path between u and v
    u = random.randint(0, len(mat) - 1)
    v = random.randint(0, len(mat) - 1)
    while u == v:
        v = random.randint(0, len(mat) - 1)
    print(f'The shortest path from {u} to {v}: ', end='')
    print(path[u][v]) if u < len(mat) and v < len(mat) and len(path[u][v]) > 0 else print("No...")


def checkComps():
    mat = initInt()
    print("Weight matrix before FW:")
    printMatrix(mat)
    buildFWWeightMatrix(mat)
    print("Weight matrix after FW:")
    printMatrix(mat)

    print("Is the graph connected?", isConnected(mat))

    res = connectComponentsOfGraph(mat)
    print("Number of components =", res[0])
    for i in range(res[0]):
        print("Component number", i, ", vertices:", res[1][i])


def printMatrix(mat: typing.List[typing.List[int]]):
    for i in range(len(mat)):
        print(mat[i])


if __name__ == '__main__':
    # checkFW()
    # checkComps()
    check_weight_matrices()
