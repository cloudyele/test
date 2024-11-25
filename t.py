import sys

def min_shot(i, s):
    n = len(s)
    dp = [[float('inf')] * n for _ in range(n)]

    for l in range(n):
        dp[l][l] = 1

    for l in range(n - 1):
        dp[l][l + 1] = 1 if s[l] == s[l + 1] else 2

    for length in range(3, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            if s[l] == s[r]:
                dp[l][r] = dp[l + 1][r - 1]
            for k in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
            if s[l] == s[l + 1]:
                dp[l][r] = min(dp[l][r], dp[l + 2][r] + 1)

    return dp[0][n - 1]

num_line = int(sys.stdin.readline())
for i in range(num_line):
    color = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(i, color))
