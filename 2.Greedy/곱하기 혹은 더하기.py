def solution():
    input_str = list(map(int, list("567")))

    answer = input_str[0]
    for cur in range(1, len(input_str)):
        if answer != 0 and input_str[cur] != 0:
            answer *= input_str[cur]
        else:
            answer += input_str[cur]

    print(answer)

solution()
