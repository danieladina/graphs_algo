# Floyd Warshall Algorithm for finding the shortest path between all the pairs of vertices
# in a vertex weighted graph.

import typing
import math
import random

INF = math.inf


def vertexWeightArray2edgeWeightMatrix(vertexWeight: typing.List[int], mat: typing.List[typing.List[bool]]) -> \
        typing.List[typing.List[int]]:
    '''
    Building an edge weight matrix from a vertex weight array and a boolean matrix of edges
    :param vertexWeight: an array of vertex's weight
    :param mat: a boolean matrix of edges
    :return: an edge weight matrix
    '''
    n = len(mat)
    matWEdges = [[(vertexWeight[i] + vertexWeight[j]) if mat[i][j] and i != j else INF for j in range(n)]
                 for i in range(n)]
    for i in range(n):
        matWEdges[i][i] = 0

    # print("Matrix of edge's weights:")
    # printMatrix(matWEdges)
    return matWEdges


def edgeWeightMatrix2VertexWeightMatix(vertexWeight: typing.List[int], matWEdges: typing.List[typing.List[int]]) -> \
        typing.List[typing.List[int]]:
    '''
    Building a vertex weighted matrix from a vertex weight array and an edge's weighted matrix
    :param vertexWeight: an array of vertices weights
    :param matWEdges: a matrix of edge's weights
    :return: a matrix of vertices weights
    '''
    n = len(matWEdges)
    matWVertices = [
        [(matWEdges[i][j] + vertexWeight[i] + vertexWeight[j]) // 2 if matWEdges[i][j] != INF else INF for j in
         range(n)]
        for i in range(n)]
    return matWVertices


def vertexWeightMatrix2edgeWeightMatrix(vertexWeight: typing.List[int], matWVertices: typing.List[typing.List[int]]) -> \
        typing.List[typing.List[int]]:
    '''
    Building an edge's weighted matrix from a vertex weighted array and a vertices weighted matrix
    :param vertexWeight: an array of vertices weights
    :param matWVertices: a matrix of vertices weights
    :return: a matrix of edge's weights
    '''
    n = len(matWVertices)
    matWEdges = [
        [(2 * matWVertices[i][j] - vertexWeight[i] - vertexWeight[j]) if matWVertices[i][j] != INF else INF for j in
         range(n)]
        for i in range(n)]
    return matWEdges


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
        mat[i][i] = 0
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


#       (1)------(2)
#       |         |
#       |         |
#       |_________|
#      (3)       (4)
def initB1():
    mat = [[True, True, True, False],
           [True, True, False, True],
           [True, False, True, True],
           [False, True, True, True]]
    return mat


def initB2():
    mat = [[True, False, False, False],
           [False, True, True, True],
           [False, True, True, True],
           [False, True, True, False]]
    return mat


def check_weight_matrices():
    list_matrices = [initB1(), initB2()]
    for i in list_matrices:
        checkFWVertecesWeightToEdgesWeght(i)
        print()


def checkFWVertecesWeightToEdgesWeght(bm=initB1()):
    print("Check Floyd-Warshall algorithm for the Vertex Weighted Graph:")
    vertex_weighted_list = [1, 2, 3, 4]
    print("Vertex Weighted Array:", vertex_weighted_list)
    print("Boolean matrix of a graph:")
    printMatrix(bm)
    mat = vertexWeightArray2edgeWeightMatrix(vertex_weighted_list, bm)
    print("Step 1: Edge Weighted matrix before FW:")
    printMatrix(mat)

    path = buildPathMatrix(mat)
    print("Step 2: Matrix of prices after Floyd-Warshall algorithm:")
    printMatrix(mat)

    matWeightVert = edgeWeightMatrix2VertexWeightMatix(vertex_weighted_list, mat)
    print("Step 3: Matrix of vertices weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightVert)

    matWeightEdge = vertexWeightMatrix2edgeWeightMatrix(vertex_weighted_list, matWeightVert)
    print("Step 4: Matrix of of edges weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightEdge)

    print("Path matrix after Floyd-Warshall algorithm:")
    printMatrix(path)

    print("Is the graph connected?", isConnected(mat) and isConnectedComplexN(mat))

    # the shortest path between u and v
    u = random.randint(0, len(mat) - 1)
    v = random.randint(0, len(mat) - 1)
    while u == v:
        v = random.randint(0, len(mat) - 1)
    print(f'The shortest path from {u} to {v}: ', end='')
    print(path[u][v]) if u < len(mat) and v < len(mat) and len(path[u][v]) > 0 else print("No...")


def checkFW(bm=initB1()):
    print("Check Floyd-Warshall algorithm for the Vertex Weighted Graph:")
    vertex_weighted_list = [1, 2, 3, 4]
    print("Vertex Weighted Array:", vertex_weighted_list)
    print("Boolean matrix of a graph:")
    printMatrix(bm)
    mat = vertexWeightArray2edgeWeightMatrix(vertex_weighted_list, bm)
    print("Step 1: Edge Weighted matrix before FW:")
    printMatrix(mat)

    buildFWWeightMatrix(mat)
    print("Step 2: Matrix of prices after Floyd-Warshall algorithm:")
    printMatrix(mat)

    matWeightVert = edgeWeightMatrix2VertexWeightMatix(vertex_weighted_list, mat)
    print("Step 3: Matrix of vertices weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightVert)

    matWeightEdge = vertexWeightMatrix2edgeWeightMatrix(vertex_weighted_list, matWeightVert)
    print("Step 4: Matrix of of edges weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightEdge)


def checkComps(bm=initB1()):
    vertex_weighted_list = [1, 2, 3, 4]
    print("Vertex Weighted Array:", vertex_weighted_list)
    print("Boolean matrix of a graph:")
    printMatrix(bm)
    mat = vertexWeightArray2edgeWeightMatrix(vertex_weighted_list, bm)
    print("Step 1: Edge Weighted matrix before FW:")
    printMatrix(mat)

    buildFWWeightMatrix(mat)
    print("Step 2: Matrix of prices after Floyd-Warshall algorithm:")
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
    # checkComps(initB2())
    check_weight_matrices()
