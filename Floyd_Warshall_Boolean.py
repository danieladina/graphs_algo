import typing


# Floyd Warshall Algorithm

def buildFWBooleanMatrix(bm: typing.List[typing.List[bool]]):
    '''
    Problem 1: Floyd-Warshall algorithm implementation
	Build transitive closure of a graph
	Complexity: O(n^3)
    :param bm: a boolean matrix
    :return:
    '''
    n = len(bm)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                bm[i][j] = bm[i][j] or (bm[i][k] and bm[k][j])


def buildPathMatrix(bm: typing.List[typing.List[bool]]) -> typing.List[typing.List[str]]:
    '''
    Problem 2: Constructing a path by Floyd-Warshall algorithm
    Complexity: O(n^3)
    :param bm: a boolean matrix
    :return: a path matrix
    '''
    n = len(bm)
    for i in range(n):
        for j in range(n):
            if i == j:
                bm[i][j] = True
    # path matrix initialization:
    pathMat = [[str(i) + "->" + str(j) if bm[i][j] else "" for j in range(n)] for i in range(n)]
    print("Path matrix before FW:")
    printMatrix(pathMat)

    # path matrix building:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not bm[i][j] and (bm[i][k] and bm[k][j]):
                    pathMat[i][j] = pathMat[i][k] + "," + pathMat[k][j]
                bm[i][j] = bm[i][j] or (bm[i][k] and bm[k][j])
    return pathMat


def connectComponentsOfGraphBoolean(bm: typing.List[typing.List[bool]]) -> [int, typing.List[typing.List[int]]]:
    '''
    Problem 3: Find a number of connected component
    and get a list of vertices in the each connected components
    :param bm: a boolean matrix
    :return:
    '''
    # first, find a number of connected components
    # in the undirected graph (square symmetric matrix)
    n = len(bm)
    connectComp = [0 for i in range(n)]
    numComponentes = 0
    for i in range(n):
        if connectComp[i] == 0:
            numComponentes += 1
            # connectComp[i] - a component number of the vertex i
            connectComp[i] = numComponentes
        for j in range(i+1,n):
            # vertex j is not defined yet
            if connectComp[j] == 0 and bm[i][j]:
                # the vertex j was defined and and the path between (i,j) exists
                connectComp[j] = numComponentes

    #last, get a vertice's list of each connected components
    vertexInComponent = [[] for i in range(numComponentes)]
    for i in range(len(connectComp)):
        index = connectComp[i] - 1
        vertexInComponent[index].append(i)

    #printMatrix(vertexInComponent)
    return numComponentes, vertexInComponent



def isConnected(bm: typing.List[typing.List[bool]]) -> bool:
    '''
    Problem 4: Check the connectivity of the graph
    Complexity: O(n^2)
    :param bm: a boolean matrix
    :return: true if a graph is connected otherwise false
    '''
    n = len(bm)
    ans = True
    for i in range(n):
        if ans:
            for j in range(n):
                if ans:
                    if not bm[i][j]:
                        ans = False
    return ans

def isConnectedComplexN(bm: typing.List[typing.List[bool]]) -> bool:
    '''
    Problem 4: Check the connectivity of the graph
    Complexity: O(n)
    :param bm: a boolean matrix
    :return: true if a graph is connected otherwise false
    '''
    n = len(bm)
    ans = True
    for i in range(n):
        if not bm[0][i]:
            ans = False
    return ans

def initBool():
    mat = [[False, True, False, False, True],
           [True, False, True, False, False],
           [False, True, False, True, False],
           [False, False, True, False, True],
           [True, False, False, True, False]]
    return mat

#      V4
#     / \
#    /   \
#   /____ \
#  V0    V5
# V6 ------V3
# |       |
# | _____ |
# V1     V2


def Init01():
    T = [[False, False, False, False, True, True, False],
         [False, False, True, False, False, False, True],
         [False, True, False, True, False, False, False],
         [False, False, True, False, False, False, True],
         [True, False, False, False, False, True, False],
         [True, False, False, False, True, False, False],
         [False, True, False, True, False, False, False]]

    return T


def checkFWBooleanMatrix():
    mat = initBool()
    print("Boolean matrix before FW:")
    printMatrix(mat)
    buildFWBooleanMatrix(mat)
    print("Boolean matrix after FW:")
    printMatrix(mat)

    path = buildPathMatrix(initBool())
    print("Path matrix after FW:")
    printMatrix(path)

    print("Is the graph connected?", isConnected(mat))


def checkComps():
    mat = Init01()
    print("Boolean matrix before FW:")
    printMatrix(mat)
    buildFWBooleanMatrix(mat)
    print("Boolean matrix after FW:")
    printMatrix(mat)

    print("Is the graph connected?", isConnected(mat))

    res = connectComponentsOfGraphBoolean(mat)
    print("Number of components =", res[0])
    for i in range(res[0]):
        print("Component number", i, ", vertices:", res[1][i])

def printMatrix(mat: typing.List[typing.List[bool]]):
    for i in range(len(mat)):
        print(mat[i])

if __name__ == '__main__':
    #checkFWBooleanMatrix()
    checkComps()
