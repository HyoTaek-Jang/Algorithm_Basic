for _ in range(int(input())):
    N = int(input())
    _dp = [[0,0] for _ in range(41)]
    _dp[0] = [1,0]
    _dp[1] = [0,1]

    for i in range(2, N+1):
        _dp[i] = [_dp[i-1][0] + _dp[i-2][0], _dp[i-1][1] + _dp[i-2][1]]

    print(_dp[N][0], _dp[N][1])
