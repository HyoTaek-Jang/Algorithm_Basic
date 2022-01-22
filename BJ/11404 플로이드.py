import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dp = [[1e9] * (n + 1) for _ in range(n + 1)]

for start in range(1, n+1):
    dp[start][start] = 0

for _ in range(m):
    start, end, weight = map(int, (sys.stdin.readline().strip().split()))
    dp[start][end] = min(weight, dp[start][end])

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid][end])

for row in range(1,n+1):
    for col in range(1, n+1):
        if dp[row][col] == 1e9:
            print("0", end=" ")
            continue
        print(dp[row][col], end=" ")
    print()

