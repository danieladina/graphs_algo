import typing


'''
Output:
m = 1 # first bottle
n = 2 # second bottle
[True, False, True, True, False, False]
[True, True, True, True, True, False]
[True, False, True, False, True, True]
[True, True, False, True, False, True]
[False, True, True, True, True, True]
[False, False, True, True, False, True]
'''


# the matrix initialization
def init_boolean_bottles_matrix(m: int, n: int) -> typing.List[typing.List[bool]]:
    size_mat = (m + 1) * (n + 1)
    bottles_mat = [[False] * size_mat for i in range(size_mat)]
    # first method:
    for i in range(m + 1):
        for j in range(n + 1):
            index = get_index(i, j, n)
            # *****  1.  (i, j)  --> (0, j):
            bottles_mat[index][get_index(0, j, n)] = True
            # *****  2.  (i, j)  --> (m, j):
            bottles_mat[index][get_index(m, j, n)] = True
            # *****  3.  (i, j) -->  (i, 0):
            bottles_mat[index][get_index(i, 0, n)] = True
            # *****  4.  (i, j) -->  (i, n):
            bottles_mat[index][get_index(i, n, n)] = True
            # *****  5.  (i, j) --> (max(0, i + j - n), min(n, i + j)):
            index_to = get_index(max(0, i + j - n), min(n, i + j), n)
            bottles_mat[index][index_to] = True
            # *****  6.  (i, j) --> (min(m, i + j), max(0, i + j - m)):
            index_to = get_index(min(m, i + j), max(0, i + j - m), n)
            bottles_mat[index][index_to] = True

    # # second method:
    # for index in range(size_mat):
    #     i = get_i(index, n)
    #     j = get_j(index, n)
    #     bottles_mat[index][get_index(0, j, n)] = True
    #     bottles_mat[index][get_index(i, 0, n)] = True
    #     bottles_mat[index][get_index(m, j, n)] = True
    #     bottles_mat[index][get_index(i, n, n)] = True
    #     bottles_mat[index][get_index(i + j - (min(i + j, n)), min(i + j, n), n)] = True
    #     bottles_mat[index][get_index(min(i + j, m), i + j - min(i + j, m), n)] = True
    return bottles_mat


# the index calculation for rows
def get_index(i: int, j: int, n: int) -> int:
    '''
    calculation the index for rows
    :param i: row index
    :param j: column index
    :param n: number columns
    :return: index for rows
    '''
    return (n + 1) * i + j


def get_i(k: int, n: int) -> int:
    return k // (n + 1)


def get_j(k: int, n: int) -> int:
    return k % (n + 1)


# Constructing paths for a content state index of a pair of bottles
def FWAlgorithmBool(bm: typing.List[typing.List[bool]]) -> typing.List[typing.List[str]]:
    '''
    Constructing a path for a content state index of a pair of bottles
    by Floyd-Warshall algorithm
    Complexity: O(n^3)
    '''
    n = len(bm)
    # path matrix initialization:
    pathMat = [[str(i) + "->" + str(j) if bm[i][j] else "" for j in range(n)] for i in range(n)]
    # print("Path matrix before FW:")
    # print_boolean_bottles_matrix(pathMat)

    # path matrix building:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not bm[i][j] and (bm[i][k] and bm[k][j]):
                    pathMat[i][j] = pathMat[i][k] + pathMat[k][j]
                bm[i][j] = bm[i][j] or (bm[i][k] and bm[k][j])
    return pathMat


# Constructing paths for the content states of a pair of bottles
def FWBooleanForBottle(bm: typing.List[typing.List[bool]], n: int) -> typing.List[typing.List[str]]:
    '''
    Constructing a path for the content states of a pair of bottles
    by Floyd-Warshall algorithm
    Complexity: O(n^3)
    '''

    # path matrix initialization:
    pathMat = [["(" + str(get_i(i, n)) + "," + str(get_j(i, n)) + ")->("
                + str(get_i(j, n)) + "," + str(get_j(j, n)) + ")" if bm[i][j]
                else "" for j in range(len(bm))] for i in range(len(bm))]
    print("Path matrix before FW:")
    print_boolean_bottles_matrix(pathMat)

    # path matrix building:
    for k in range(len(bm)):
        for i in range(len(bm)):
            for j in range(len(bm)):
                if not bm[i][j] and (bm[i][k] and bm[k][j]):
                    pathMat[i][j] = pathMat[i][k] + pathMat[k][j]
                bm[i][j] = bm[i][j] or (bm[i][k] and bm[k][j])

    return pathMat

# checking an existence of a path between content states of a pair of bottles
def isExistPath(i1: int, j1: int, i2: int, j2: int, mat: typing.List[typing.List[bool]],
                paths: typing.List[typing.List[str]], n: int, m: int) -> None:
    '''
    This function checks whether there is a path between content states of a pair of bottles.
    If yes, it returns this path.
    :param i1: an initial content state of one of bottles
    :param j1: an initial content state of the other bottle
    :param i2: a final content state of one of bottles
    :param j2: a final content state of the other bottle
    :param mat: a boolean matrix of the transition existence between content states of a pair of bottles
    :param paths: a path matrix of a transition between content states of a pair of bottles
    :param n: a capacity of one of bottles (the smallest)
    :param m: a capacity of the other bottle (the biggest)
    :return: print a path if it exits otherwise print "No.."
    '''
    minimum = min(i1,j1)
    maximum = max(i1,j1)
    i1 = maximum
    j1 = minimum

    minimum = min(i2,j2)
    maximum = max(i2,j2)
    i2 = maximum
    j2 = minimum

    print("Is there a path from (" + str(i1) + "," + str(j1) + ") to (" + str(i2) + "," + str(j2) + ")?")
    if i1 > m or i2 > m or j1 > n or j2 > n:
        print("NO...")
        return
    i = get_index(i1, j1, n)
    j = get_index(i2, j2, n)
    print("YES! " + str(paths[i][j]) if mat[i][j] else "NO..")


def print_boolean_bottles_matrix(mat):
    # print(mat)
    for i in range(len(mat)):
        print(mat[i])

##############################
def check_boolean_bottles_matrix():
    list_bottles = [[1, 1],
                    [2, 1],
                    [2, 2],
                    [3, 2],
                    [3, 5]]
    for i in range(len(list_bottles)):
        m = list_bottles[i][0]
        n = list_bottles[i][1]
        print(f'\nFor the first bottle m = {m} and the second bottle n = {n}, the boolean bottles matrix:')
        print_boolean_bottles_matrix(init_boolean_bottles_matrix(m, n))


def check_bottle_wf(m=2, n=1):
    #     m = 2 # first bottle
    #     n = 1 # second bottle
    m = n if n > m else m
    mat = init_boolean_bottles_matrix(m, n)
    print(f'For the first bottle with a capacity m = {m} and for the second bottle with a capacity n = {n}')
    print("--------Before FW Algoritm---------")
    print("the boolean bottles matrix is:")
    print_boolean_bottles_matrix(mat)

    # paths = FWAlgorithmBool(mat)      # paths for a content state index of a pair of bottles
    paths = FWBooleanForBottle(mat, n)  # paths for the content states of a pair of bottles
    print("--------After FW Algoritm---------")
    print("the boolean bottles matrix is:")
    print_boolean_bottles_matrix(mat)
    # print("Path Matrix for a content state index of a pair of bottles:")
    print("Path Matrix for the content states of a pair of bottles:")
    print_boolean_bottles_matrix(paths)

    isExistPath(0, 0, 0, 4, mat, paths, n, m)


if __name__ == '__main__':
    # check_boolean_bottles_matrix()
    check_bottle_wf(5, 3)
