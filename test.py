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

print(solution('12948026141',2))