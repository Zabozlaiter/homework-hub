n = 3
m = 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        res[j][n - 1 - i] = c[i][j]

for i in range(m):
    print(*res[i])