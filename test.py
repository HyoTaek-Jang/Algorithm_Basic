def solution(array, commands):
    answer = []
    for i in commands:
        temp = sorted(array[i[0]-1:i[1]-1])
        answer.append(temp[i[2]])
    return answer

solution([1,5,2,6,3,7,4],[[2,5,3]])