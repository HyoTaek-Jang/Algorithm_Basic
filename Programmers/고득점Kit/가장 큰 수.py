def solution(numbers):
    str_list = []
    for idx in range(len(numbers)):
        temp = str(numbers[idx]) * 4

        str_list.append([temp[:4], idx])

    str_list.sort(reverse=True, key=lambda x: int(x[0]))

    answer = ""
    for cur in str_list:
        answer += str(numbers[cur[1]])

    if int(answer) == 0:
        return "0"
    return answer