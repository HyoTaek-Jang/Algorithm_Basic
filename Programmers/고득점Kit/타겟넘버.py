def solution(numbers, target):
    answer = calcul(1, -numbers[0], numbers, 0, target)
    answer = calcul(1, numbers[0], numbers, answer, target)

    return answer


def calcul(idx, value, numbers, answer, target):
    if idx == len(numbers):
        if value == target:
            answer += 1
        return answer

    answer = calcul(idx + 1, value + numbers[idx], numbers, answer, target)
    answer = calcul(idx + 1, value - numbers[idx], numbers, answer, target)

    return answer