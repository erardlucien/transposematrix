import transpose1


def transpose(matrix, trans_m):
    if type(matrix[0]) == int:
        transpose1.transposeOneDimensionArray(matrix, trans_m)
    elif type(matrix[0][0]) == int:
        if len(matrix) == len(matrix[0]):
            transpose1.transposeWhenrowIsEqualTocol(matrix, trans_m)
        elif len(matrix) < len(matrix[0]):
            transpose1.transposeWhenrowIsSmallerThancol(matrix, trans_m)
        else:
            transpose1.transposeWhenrowIsBiggerThancol(matrix, trans_m)
    else:
        print("It is not defined in this function!")
