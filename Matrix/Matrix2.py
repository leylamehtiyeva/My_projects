# Example
"""
Input:
2
3
It
is
not
your
birthday
party

Output:
It is not
your birthday party

It your
is birthday
not party"""


n = int(input())
m = int(input())
matrix = [[0]*m for _ in range(n)]


for i in range(n):
    for j in range(m):
        matrix[i][j] = input()


for row in matrix:
    print(*row)
print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
