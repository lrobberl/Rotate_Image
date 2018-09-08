
def cyclicSwap(m, init_i, init_j):
    matrixDim = len(m)
    limit_y = matrixDim - 1 - init_j
    limit_x = matrixDim - 1 - init_i
    offset = 0

    while offset < (matrixDim - 2*init_i) - 1:
        # swap with the horizontal opposite
        m[init_i][init_j+offset], m[init_i+offset][limit_y] = m[init_i+offset][limit_y], m[init_i][init_j+offset]
        # swap diagonal opposites
        m[init_i][init_j+offset], m[limit_x][limit_y-offset] = m[limit_x][limit_y-offset], m[init_i][init_j+offset]
        # swap vertical opposites
        m[init_i][init_j+offset], m[limit_x-offset][init_j] = m[limit_x-offset][init_j], m[init_i][init_j+offset]

        offset += 1

    # in case of an odd dimension, we have to swap one more time
    # if (matrixDim - 2*init_i) % 2 == 1:
    #     m[init_i][init_j+offset], m[init_i+offset][limit_y] = m[init_i+offset][limit_y], m[init_i][init_j+offset]
    #     m[init_i][init_j+offset], m[limit_x][limit_y-offset] = m[limit_x][limit_y-offset], m[init_i][init_j+offset]
    #     m[init_i][init_j+offset], m[limit_x-offset][init_j] = m[limit_x-offset][init_j], m[init_i][init_j+offset]

    return m



"""

We start from the outermost square, swapping in a cyclic motion all the elements
When proceeding inward, the squares get smaller and smaller (nCols decrease by 2)

"""

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

matrixDimension = len(matrix)

print("This is the %dx%d matrix:\n" % (matrixDimension,matrixDimension))
for x in matrix:
    for y in x:
        print("%d\t" % y, end="")
    print("\n")

i = 0
while i < matrixDimension/2:
    m = cyclicSwap(matrix, i, i)
    i += 1

print("Here's the matrix rotated by 90 degrees clockwise:\n")
for x in matrix:
    for y in x:
        print("%d\t" % y, end="")
    print("\n")

