import sys

def sol(N):
    d = [0]*1000
    d[0] = 1
    d[1] = 3

    for i in range(2,N):
        d[i] = d[i-1] + d[i-2]*3

    print(d[N-1]%796796)

# sol(765)

def sol2():
    N,M = map(int, sys.stdin.readline().split())

    token = [0]*N
    money = [10001]*(M+1)
    for i in range(N):
        token[i] = int(sys.stdin.readline())
    token.sort(reverse=True)

    for j in token: #7, 5, 3
        if M-j >= 0:
            money[j] = 1

    for i in range(1,M+1): # i원일때 몇개가 필요한가 8 =  5 3
        for j in token: #
            if i-j >= 0 and money[i-j] > 0:
                money[i] = min(money[i-j] + 1, money[i])

    if money[M] == 10001:
        print(-1)
    print(money[M])

# sol2()