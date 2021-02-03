def solution(s):
    words = s.split(" ")
    answers = []
    for word in words:
        c = []
        for i in range(len(word)):
            if i % 2 == 0:
                c.append(word[i].upper())
            else:
                c.append(word[i].lower())
        answers.append(''.join(c))
    answer = ' '.join(answers)
    return answer