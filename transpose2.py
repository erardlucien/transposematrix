matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  # original matrix
trans_m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # trans_m := transposed matrix

print("matrix:")
print(matrix)
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        trans_m[x][y] = matrix[y][x]
print("trans_m:")
print(trans_m)
print()

matrix1 = 3*[[x for x in range(3)]]  # original matrix1

trans_m1 = []  # trans_m1 := transposed matrix1
row = []  # row
print("matrix1:")
print(matrix1)
print()

for x in range(len(matrix1)):
    print("row[", x, "]", end=":")
    for y in range(len(matrix1[0])):
        row.append(matrix1[y][x])  # row take every element of transposed row
        # of the matrix1
        if y == len(matrix1[0]) - 1:
            print(row[y], end=".")
            trans_m1.append(row[:])
            print()
            print("trans_m1:")
            print(trans_m1)
            row = []
            print()
        else:
            print(row[y], end=", ")

print("trans_m1:")
print(trans_m1)

matrix2 = 2*[[x for x in range(1, 4)]]
# row is smaller than column
matrix3 = []
for x in range(len(matrix2[0])):
    if x < len(matrix2):
        matrix3.append(matrix2[x])
    else:
        matrix3.append([0 for x in range(len(matrix2[0]))])

trans_m2 = []
trans_m3 = []

print("matrix2:")
print(matrix2)
print("matrix3:")
print(matrix3)

for x in range(len(matrix3)):
    for y in range(len(matrix3[0])):
        row.append(matrix3[y][x])
        if y == len(matrix3[0]) - 1:
            trans_m3.append(row[:])
            row = []
print("trans_m3:")
print(trans_m3)

for x in range(len(matrix2[0])):
    for y in range(len(matrix2)):
        row.append(trans_m3[x][y])
        if y == len(matrix2) - 1:
            trans_m2.append(row[:])
            row = []

print("trans_m2:")
print(trans_m2)

matrix4 = 5*[[x for x in range(1, 4)]]
# row is bigger than column
matrix5 = []
trans_m4 = []
trans_m5 = []

print("matrix4:")
print(matrix4)

for x in range(len(matrix4)):
    for y in range(len(matrix4[0])):
        row.append(matrix4[x][y])
        if y == len(matrix4[0]) - 1:
            for z in range(len(matrix4) - len(matrix4[0])):
                row.append(0)
            matrix5.append(row[:])
            row = []

print("matrix5:")
print(matrix5)


for x in range(len(matrix5)):
    for y in range(len(matrix5[0])):
        row.append(matrix5[y][x])
        if y == len(matrix5[0]) - 1:
            trans_m5.append(row[:])
            row = []

print("trans_m5:")
print(trans_m5)

for x in range(len(matrix4[0])):
    for y in range(len(matrix4)):
        row.append(trans_m5[x][y])
        if y == len(matrix4) - 1:
            trans_m4.append(row[:])
            row = []

print("trans_m4:")
print(trans_m4)
