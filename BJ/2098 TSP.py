import sys

N = int(sys.stdin.readline())
dp = [[None] * (1 << N) for _ in range(N)]

for row in range(N):
    cur_list = list(map(int, sys.stdin.readline().strip().split()))
    for col in range(N):
        if row == col:
            dp[col][row] = cur_list[col]
            continue
        dp[col][(1 << row) | (1 << col)] = cur_list[col]

print(dp)
print((1 << 0) | (1 << 0))