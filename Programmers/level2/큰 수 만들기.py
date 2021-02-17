# try 1

# 10번 시간초과 12번 런타임 오류
'''
def solution(number, k):
    answer = ''
    while k!=0:
        temp = [ i for i in number[:k+1]]
        _max = max(temp)
        idx = number.index(_max)
        answer += _max
        number = number[idx+1:]
        k -= idx
    answer += number
    return answer
'''

# try2 9 만나면 그게 최고니까 브레이크 걸어버렸는데 더 오래걸림. 슬라이싱이 더 효율적인가봄
'''
def solution(number, k):
    answer = ''
    while k!=0:
        _v = 0
        temp = []
        for i in range(k+1):
            temp.append(number[i])
            if number[i] == 9: break
        _max = max(temp)
        idx = number.index(_max)
        answer += _maxs
        number = number[idx+1:]
        k -= idx
    answer += number    
    return answer
'''

# try3 for문을 1번만 사용, 동일하게 10번 시간초과
'''
def solution(number, k):
    answer = ''
    _temp = [i for i in number]
    while k!=0:
        temp = _temp[:k+1]
        _max = max(temp)
        idx = temp.index(_max)
        answer += _max
        _temp = _temp[idx+1:]
        k -= idx
    answer += ''.join(_temp)
    return answer
'''

# try4 max를 사용안함 동일하게 10, 12 실패 시간초과 1-4 중엔 젤 빠름
'''
def solution(number, k):
    answer = ''
    _temp = [i for i in number]
    while k!=0:
        temp = _temp[:k+1]
        idx = 0
        for i in range(9,-1,-1):
            i = str(i)
            if i in temp:
                answer += i
                idx = temp.index(i)
                break
        k -= idx
        _temp = _temp[idx+1:]
    answer += ''.join(_temp)
    return answer
'''

# try5 개자식들 누가 이기나 해보자 10번 뚫음 12번 실패;;;; 아예 한번 포문 돌리는거로 끝냄 맨 끝자리 확인하면서 빼고 넣고 ㅇㅋ?
'''
def solution(number, k):
    temp = [number[0]]
    for i in range(1,len(number)):
        if temp[len(temp)-1]<number[i]:
            while k > 0  and len(temp)>0 and temp[len(temp)-1]<number[i]:
                temp.pop()
                k -= 1
            temp.append(number[i])
        else:
            temp.append(number[i])
    answer = ''.join(temp)
    return answer

'''

# try6 이김. 마지막에 k로 안잘라줌
def solution(number, k):
    temp = [number[0]]
    for i in range(1, len(number)):
        if temp[len(temp) - 1] < number[i]:
            while k > 0 and len(temp) > 0 and temp[len(temp) - 1] < number[i]:
                temp.pop()
                k -= 1
        temp.append(number[i])

    if k != 0:
        temp = temp[:-k]
    answer = ''.join(temp)
    return answer