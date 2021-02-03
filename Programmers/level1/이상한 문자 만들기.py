def solution(s):
    words = s.split(' ')
    answer = ''
    for word in words:
        newWord = ""
        for i in range(len(word)):
            if i % 2 == 0:
                newWord += word[i].upper()
            else:
                newWord += word[i].lower()
        answer += newWord + " "

    answer = answer[:len(answer) - 1]

    return answer