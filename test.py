def soldier(N,list):
    _dp = [0]*100
    _dp[0] = list[0]
    _dp[1] = max(list[0], list[1])

    for i in range(2,N):
        _dp[i] = max(_dp[i-2]+list[i], _dp[i-1])

    print(_dp[N-1])

soldier(5,[1,3,1,5,10])