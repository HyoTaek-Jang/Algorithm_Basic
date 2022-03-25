N = int(input())

dp = [[0, 0, 0] for _ in range(N + 1)]
dp[1] = [1, 1, 1]
# 왼, 오, 공백

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][0]) % 9901

print((sum(dp[N])) % 9901)
