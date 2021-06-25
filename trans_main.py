import transpose

matrix = 4 * [[x for x in range(4)]]
matrix1 = 2 * [[x for x in range(4)]]
matrix2 = 5 * [[x for x in range(3)]]
matrix3 = [[[1, 23, 4],  [1, 2, 3], [1, 5, 6]],
           [[1, 23, 4], [1, 2, 3], [1, 5, 6]]]
array = [x for x in range(1, 4)]
trans_m = []

print("matrix:")
print(matrix)
transpose.transpose(matrix, trans_m)
print("trans_m:")
print(trans_m)
trans_m = []
print("matrix1:")
print(matrix1)
transpose.transpose(matrix1, trans_m)
print("trans_m:")
print(trans_m)
trans_m = []
print("matrix2:")
print(matrix2)
transpose.transpose(matrix2, trans_m)
print("trans_m:")
print(trans_m)
trans_m = []
print("array:")
print(array)
transpose.transpose(array, trans_m)
print("trans_m:")
print(trans_m)
trans_m = []
print("matrix3:")
print(matrix3)
transpose.transpose(matrix3, trans_m)
print("trans_m:")
print(trans_m)
print(matrix3[0].index([1, 5, 6]))
