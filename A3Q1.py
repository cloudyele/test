import sys


def min_shot(color):
    n = len(color)
    count = [[float('inf')] * n for _ in range(n)]

    for l in range(n):
        count[l][l] = 1

    for l in range(n - 1):
        if color[l] == color[l + 1]:
            count[l][l + 1] = 1
        else:
            count[l][l + 1] = 2
# -------------------------

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if color[i] == color[j]:
                count[i][j] = count[i + 1][j - 1]

            for k in range(i, j):
                count[i][j] = min(count[i][j], count[i][k] + count[k + 1][j])

            if color[i] == color[i + 1]:
                count[i][j] = min(count[i][j], count[i + 2][j] + 1)

    return count[0][n - 1]


num_line = int(sys.stdin.readline())
for i in range(num_line):
    color = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(color))
