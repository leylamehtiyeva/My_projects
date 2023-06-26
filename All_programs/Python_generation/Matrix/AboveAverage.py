

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def mean(lst):
    return sum(lst) / len(lst)


for row in matrix:
    row_mean = mean(row)
    res = len([x for x in row if x > row_mean])
    print(res)