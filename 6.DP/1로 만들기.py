K = int(input())

_dp = [1e9] * (K + 1)
_dp[1] = 0
# 5,3,2 |  -1

for i in range(2, K + 1):
    if i >= 3 and i % 3 == 0:
        _dp[i] = min(_dp[i // 3] + 1, _dp[i])
    if i >= 2 and i % 2 == 0:
        _dp[i] = min(_dp[i // 2] + 1, _dp[i])
    if i > 1:
        _dp[i] = min(_dp[i - 1] + 1, _dp[i])

print(_dp[K])
