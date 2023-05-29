n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

left_quarter = sum([matrix[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)])
upper_quarter = sum([matrix[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)])
right_quarter = sum([matrix[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)])
down_quarter = sum([matrix[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)])
print(f"Upper quarter: {upper_quarter}")
print(f"Right quarter: {right_quarter}")
print(f"Down quarter: {down_quarter}")
print(f"Left quarter: {left_quarter}")
