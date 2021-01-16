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

list = 'absc'.split()
print(list)