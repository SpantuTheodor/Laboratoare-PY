"""Given a square matrix of characters write a script that prints the string obtained by going through
 the matrix in spiral order"""
rc = int(input())

matrix = []

for i in range(rc):
    aux = []
    for j in range(rc):
        aux.append(str(input()))
    matrix.append(aux)

k = 0
i = 0
j = 0
print("")

while k < rc / 2:
    for j in range(0 + k, rc - k, 1):
        print(matrix[i][j])
    for i in range(1 + k, rc - k, 1):
        print(matrix[i][j])
    for j in range(rc - k - 2, k - 1, -1):
        print(matrix[i][j])
    for i in range(rc - 2 - k, k, -1):
        print(matrix[i][j])
    k += 1
