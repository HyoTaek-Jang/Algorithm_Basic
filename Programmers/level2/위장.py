# 놑북을 성준이네 두고 와서 그냥 이렇게 작성함
# 하튼 트라이 1은 이터레이터 써서 콤비네이션 돌리고 나온 결과를 계산했는데 시간초과
# 그래서 어떻게 계산을 줄이지 고민하다가 모든 경우를 다 더하고 아무것도 안입은 경우 1개를 빼면 되더라 성공!
def solution(clothes):
    hashMap = {}
    temp = 0
    
    for i in clothes:
        if i[1] in hashMap:hashMap[i[1]].append(i[0])
        else:hashMap[i[1]] = [i[0]]

    for i in hashMap:
        if temp == 0 : temp = len(hashMap[i])+1
        else: temp *= (len(hashMap[i])+1)

    return temp-1
