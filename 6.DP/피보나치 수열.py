def fibo(n):
    _dp = []
    _dp.append(1)
    _dp.append(1)
    for i in range(2,n):
        _dp.append(_dp[i-1]+_dp[i-2])
    return _dp[n-1]

print(fibo(99))