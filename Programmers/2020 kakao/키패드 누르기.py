def solution(numbers, hand):
    answer = ''
    temp = [-1, -2, -2]
    rank = [-1, -1, -1]
    col = [0, 0, 0]

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            temp[0] = number
        elif number in [3, 6, 9]:
            answer += 'R'
            temp[1] = number
        else:
            temp[2] = number
            for i in range(3):
                if temp[i] in [1, 2, 3]:
                    rank[i] = 1
                elif temp[i] in [4, 5, 6]:
                    rank[i] = 2
                elif temp[i] in [7, 8, 9]:
                    rank[i] = 3
                else:
                    rank[i] = 4

                if temp[i] in [1, 4, 7, -1]:
                    col[i] = 1
                elif temp[i] in [2, 5, 8, 0]:
                    col[i] = 2
                else:
                    col[i] = 3

            left = abs(rank[0] - rank[2])
            right = abs(rank[1] - rank[2])

            if col[0] == col[2]: left -= 1
            if col[1] == col[2]: right -= 1

            if left > right:
                answer += 'R'
                temp[1] = number
            elif left < right:
                answer += 'L'
                temp[0] = number
            elif hand[0] == 'r':
                answer += 'R'
                temp[1] = number
            else:
                answer += 'L'
                temp[0] = number

    return answer