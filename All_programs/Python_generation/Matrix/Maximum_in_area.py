n = 3
matrix = [[2, 4, 5], [6, 7, 8], [8, 1, 6]]

res = max([matrix[i][j] for i in range(n) for j in range(n) if
           (i > j and i <= n - 1 - j) or (i > j and i >= n - 1 - j) or (i == j)])
print(res)