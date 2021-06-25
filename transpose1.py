def transposeWhenrowIsEqualTocol(matrix, trans_m):
    # col := column
    row = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            row.append(matrix[y][x])
            if y == len(matrix[0]) - 1:
                trans_m.append(row)
                row = []


def transposeOneDimensionArray(array, trans_array):
    for x in range(len(array)):
        trans_array.append(array[x])


def setTransposedMatrix(matrix, trans_tmp, trans_m):
    # give transposed matrix when  dimension is equal to 2
    row = []
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            row.append(trans_tmp[x][y])
            if y == len(matrix) - 1:
                trans_m.append(row)
                row = []


def transposeWhenrowIsSmallerThancol(matrix, trans_m):
    trans_tmp, tmp_m = [], []
    for x in range(len(matrix[0])):
        if x < len(matrix):
            tmp_m.append(matrix[x])
        else:
            tmp_m.append([0 for x in range(len(matrix[0]))])

    transposeWhenrowIsEqualTocol(tmp_m, trans_tmp)
    setTransposedMatrix(matrix, trans_tmp, trans_m)


def transposeWhenrowIsBiggerThancol(matrix, trans_m):
    trans_tmp, tmp_m, row = [], [], []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            row.append(matrix[x][y])
            if y == len(matrix[0]) - 1:
                for z in range(len(matrix) - len(matrix[0])):
                    row.append(0)
                tmp_m.append(row)
                row = []

    transposeWhenrowIsEqualTocol(tmp_m, trans_tmp)
    setTransposedMatrix(matrix, trans_tmp, trans_m)
