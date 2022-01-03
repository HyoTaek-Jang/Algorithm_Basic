def solution():
    col, row = map(int, input().split())
    N = int(input())

    shops = []
    for _ in range(N):
        shop = list(map(int, input().split()))
        shops.append(shop)
    mine = list(map(int, input().split()))

    answer = 0
    myLocation = calculator(mine, col, row)
    for shop in shops:
        location = calculator(shop, col, row)

        if myLocation[1] == location[1] or (myLocation[0] == 0 or myLocation[0] == row) and (
                location[0] == 0 or location[0] == row):
            answer += abs(myLocation[0] - location[0])
        else:
            answer += min(myLocation[0] + location[0], row - myLocation[0] + row - location[0])

        if myLocation[0] == location[0] or (myLocation[1] == 0 or myLocation[1] == col) and (
                location[1] == 0 or location[1] == col):
            answer += abs(myLocation[1] - location[1])
        else:
            answer += min(myLocation[1] + location[1], col - myLocation[1] + col - location[1])

    print(answer)


def calculator(locations, col, row):
    if locations[0] == 1:
        return [0, locations[1]]
    elif locations[0] == 2:
        return [row, locations[1]]
    elif locations[0] == 3:
        return [locations[1], 0]
    elif locations[0] == 4:
        return [locations[1], col]


solution()

# 구현 : 시키는대로 한다. 근데 최적의 거리가 어떻게 나오는지는 조금 어려웠다. 모든 경우를 어떻게 파악하는지가 중요한듯.