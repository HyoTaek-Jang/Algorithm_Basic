def sol():
    N, K = map(int, input().split())

    _dp = [100001 for _ in range(100001)]

    # 초기세팅
    callStack = [N]
    _dp[N] = 0

    while len(callStack):
        cur = callStack.pop(0)
        if cur == K and _dp[K] != 100001:
            return print(_dp[K])

        if cur - 1 >= 0 and _dp[cur - 1] > _dp[cur] + 1:
            callStack.append(cur - 1)
            _dp[cur - 1] = _dp[cur] + 1

        if cur + 1 <= 100000 and _dp[cur + 1] > _dp[cur] + 1:
            callStack.append(cur + 1)
            _dp[cur + 1] = _dp[cur] + 1

        if cur * 2 <= 100000 and _dp[cur * 2] > _dp[cur] + 1:
            callStack.append(cur * 2)
            _dp[cur * 2] = _dp[cur] + 1

    if N == 0 and K == 0:
        _dp[K] = 0

    print(_dp[K])

sol()
