# Floyd Warshall Algorithm for finding the shortest path between all the pairs of vertices
# in a vertex-edge weighted graph.

import typing
import math
import random

INF = math.inf


def toEdgesWeights(vertexWeight: typing.List[int], edgeWeight: typing.List[typing.List[int]]) -> \
        typing.List[typing.List[int]]:
    '''
    Building an edge weight matrix from a vertex weight array and a matrix of weight's edges
    :param vertexWeight: an array of weight's vertices in the graph
    :param edgeWeight: a matrix of weight's edges in the graph
    :return: a matrix of edge's weights between two vertices
    '''
    n = len(edgeWeight)
    matWEdges = [[(2*edgeWeight[i][j] + vertexWeight[i] + vertexWeight[j]) if edgeWeight[i][j] != INF else INF for j in range(n)]
                 for i in range(n)]

    # print("Matrix of edge's weights between two vertices:")
    # printMatrix(matWEdges)
    return matWEdges


def edgeWeights2Vertex_EdgeWeights(vertexWeight: typing.List[int], matWEdges: typing.List[typing.List[int]]) -> \
        typing.List[typing.List[int]]:
    '''
	Building an vertex and edge weighted matrix from a vertex weighted array and a matrix of weight's edges
    :param vertexWeight: an array of vertices weights
    :param matWEdges: a matrix of edge's weights
    :return: a matrix of vertices and edges weights
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



def initB1():
    mat = [[0, 10,2,20,INF],
           [10,0, INF,12,1],
           [2,INF,0, 1, INF],
           [20,12,1,0,8],
           [INF,1,INF,8,0]]
    return mat


def initB2():
    mat = [[0, INF, INF,20,1],
           [0, INF, INF,20,1],
           [INF, INF,0,3,2],
           [20,6,3,0,INF],
           [1,4,2, INF,0]]
    return mat


def check_weight_matrices():
    list_matrices = [initB1(), initB2()]
    for i in list_matrices:
        checkFWVertecesWeightToEdgesWeght(i)
        print()


def checkFWVertecesWeightToEdgesWeght(wm=initB1()):
    print("Check Floyd-Warshall algorithm for the Vertex Weighted Graph:")
    vertex_weighted_list = [1,2,3,4,5]
    print("Vertex Weighted Array:", vertex_weighted_list)
    print("Matrix of a Edge Weighted Graph:")
    printMatrix(wm)
    mat = toEdgesWeights(vertex_weighted_list, wm)
    print("Step 1: Edge Weighted Matrix before FW:")
    printMatrix(mat)

    path = buildPathMatrix(mat)
    print("Step 2: Matrix of shortest-path between two vertices after Floyd-Warshall algorithm:")
    printMatrix(mat)

    matWeightVert = edgeWeights2Vertex_EdgeWeights(vertex_weighted_list, mat)
    print("Step 3: Matrix of Edge and Vertex Weighted Graph after Floyd-Warshall algorithm:")
    printMatrix(matWeightVert)

    matWeightEdge = vertexWeightMatrix2edgeWeightMatrix(vertex_weighted_list, matWeightVert)
    print("Step 4: Matrix of Edge Weighted Graph after Floyd-Warshall algorithm:")
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


def checkFW(wm=initB1()):
    print("Check Floyd-Warshall algorithm for the graph with vertice's weights and edge's weights:")
    vertex_weighted_list = [1,2,3,4,5]
    print("Vertex Weighted Array of a graph:", vertex_weighted_list)
    print("Edge Weighted Matrix of a graph:")
    printMatrix(wm)
    mat = toEdgesWeights(vertex_weighted_list, wm)
    print("Step 1: Edge Weighted matrix before FW:")
    printMatrix(mat)

    buildFWWeightMatrix(mat)
    print("Step 2: Matrix of prices after Floyd-Warshall algorithm:")
    printMatrix(mat)

    matWeightVert = edgeWeights2Vertex_EdgeWeights(vertex_weighted_list, mat)
    print("Step 3: Matrix of vertices weights and edge's weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightVert)

    matWeightEdge = vertexWeightMatrix2edgeWeightMatrix(vertex_weighted_list, matWeightVert)
    print("Step 4: Matrix of edges weights after Floyd-Warshall algorithm:")
    printMatrix(matWeightEdge)


def checkComps(bm=initB1()):
    vertex_weighted_list = [1,2,3,4,5]
    print("Vertex Weighted Array of a graph:", vertex_weighted_list)
    print("Edge Weighted Matrix of a graph:")
    printMatrix(bm)
    mat = toEdgesWeights(vertex_weighted_list, bm)
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
