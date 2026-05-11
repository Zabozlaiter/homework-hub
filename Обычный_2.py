n = 3
m = 3
b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(n // 2):
    b[i], b[n - 1 - i] = b[n - 1 - i], b[i]

for i in range(n):
    print(*b[i])