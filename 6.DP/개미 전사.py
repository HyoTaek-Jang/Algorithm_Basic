N = 4
K = [1,3,1,5]

_dp = []

_dp.append(K[0])
_dp.append(max(K[0], K[1]))

for i in range(2, N):
    _dp.append(max(_dp[i-1], _dp[i-2]+K[i]))

print(_dp[N-1])