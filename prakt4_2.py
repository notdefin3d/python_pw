n = 7
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j] = n - (j - i)

for row in matrix:
    print(row)