def solution():
    N, K = map(int, input().split())

    coins = []
    for _ in range(N):
        coins.append(int(input()))
    coins.sort(reverse=True)

    answer = 0
    for coin in coins:
        answer += K // coin
        K %= coin

    print(answer)

solution()

# 그리디 : 작은 코인으로 큰 코인을 만들 수 있기에, 큰 코인으로 나누는게 최선의 방법