K = int(input())

_dp = [1e9] * (K + 1)
history = [0] * (K + 1)
_dp[1] = 0
# 5,3,2 |  -1

for i in range(2, K + 1):
    if i >= 3 and i % 3 == 0 and _dp[i // 3] + 1 < _dp[i]:
        _dp[i] = _dp[i // 3] + 1
        history[i] = i//3
    if i >= 2 and i % 2 == 0 and _dp[i // 2] + 1 < _dp[i]:
        _dp[i] = _dp[i // 2] + 1
        history[i] = i//2

    if i > 1 and _dp[i-1] + 1 < _dp[i]:
        _dp[i] = _dp[i - 1] + 1
        history[i] = i-1

print(_dp[K])

print(K, end=" ")
temp = history[K]

while temp != 0:
    print(temp, end=" ")
    temp = history[temp]
