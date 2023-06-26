n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

res = sum([matrix[i][i] for i in range(n)])

print(res)
