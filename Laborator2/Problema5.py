"""Write a function that receives as parameter a matrix and will return the matrix obtained by
replacing all the elements under the main diagonal with 0 (zero)."""

print("Numar de linii: ")
rows = int(input())
print("Numar de coloane: ")
columns = int(input())
print("Elemente: ")

matrix = []

for i in range(rows):
    aux = []
    for j in range(columns):
        aux.append(int(input()))
    matrix.append(aux)


def diagonaltozero(matrix):
    i = 0
    for i in range(rows):
        if i + 1 < rows:
            matrix[i + 1][i] = 0


diagonaltozero(matrix)

print(" ")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print(" ")
