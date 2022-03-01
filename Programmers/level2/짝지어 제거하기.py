def solution(s):
    answer = 0
    stack = []

    cnt = 0
    for i in s:
        if cnt == 0:
            stack.append(i)
            cnt += 1
            continue
        if stack[cnt - 1] == i:
            stack.pop()
            cnt -= 1
            while cnt >= 2 and stack[cnt - 1] == stack[cnt - 2]:
                stack.pop()
                stack.pop()
                cnt -= 2
        else:
            stack.append(i)
            cnt += 1

    if cnt == 0:
        answer = 1

    return answer