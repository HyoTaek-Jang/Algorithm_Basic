'''
구현이란 머릿속에 알고리즘을 소스코드로 바꾸는 과정
구현 문제는 풀이는 쉽지만 코드로 옮기기 어려운 길이.

2차원 공간에서의 방향 벡터가 많이 활용됨
'''


def LRUD():
    N = int(input())
    plan = input().split(' ')
    x, y = 1, 1
    moveList = ['L', 'R', 'U', 'D']
    enumList = enumerate(moveList)
    movex = [-1, 1, 0, 0]
    movey = [0, 0, -1, 1]

    for move in plan:
        for i in range(4):
            if(move == moveList[i]):
                dx = x+movex[i]
                dy = y+movey[i]
                if not(dx < 1 or dy < 1 or dx > N or dy > N):
                    x, y = dx, dy
    print(x,y)

def night():
    value = input()
    col = ord(value[0])-ord('a')+1
    row = int(value[1])
    moveList = [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]
    count = 0
    for move in moveList:
        dcol = col + move[0]
        drow = row + move[1]
        if not (dcol < 1 or drow < 1 or dcol > 8 or drow > 8):
            count += 1
    print(count)


# LRUD()
# night()

# 3009번 백준 네 번째 점
# 네 점 중 두 점씩 잡으면 모두 길이가 같지 않을까 라는 가설에서 시작
# 두 번째 아이디어 : 서로 직각이 되게 두 선분을 만듬. 그리고 공통된 점에서 a1의 차를 구함. 그 다음 그 차이를 a2에 적용 시키면 a4가 나옴.
# 하아....개고생했는데 문제를 제대로 이해를 못했네... 축에 평행한.....
def fourthPoint():
    x_list = []
    y_list = []
    for i in range(3):
        x,y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    for i in range(3):
        if x_list.count(x_list[i]) == 1:
            x = x_list[i]
        if y_list.count(y_list[i]) == 1:
            y = y_list[i]
    print(x,y)

fourthPoint()