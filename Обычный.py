import random

n = 4
a = [[random.randint(10, 99) for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j > i:
            a[i][j] = 0

for i in range(n):
    print(*a[i])