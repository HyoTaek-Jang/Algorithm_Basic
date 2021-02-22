# 1차 시도 실패 시간초과 및 실패 문항 존재
# 문제 이해를 애초에 잘못함 접두어네..ㅎ

# def solution(phone_book):
#     temp = {}
#     setBook = set(phone_book)
#     for i in range(len(setBook)):
#         value = set([phone_book[i]])
#         temp[i] = setBook - value
#
#     for i in range(len(phone_book)):
#         for j in temp[i]:
#             if str(phone_book[i]) in str(j):
#                 return False
#     return True

# 2차시도 정답은 맞으나 시간초과!
# def solution(phone_book):
#     temp = {}
#     setBook = set(phone_book)
#     for i in range(len(setBook)):
#         value = set([phone_book[i]])
#         temp[i] = setBook - value
#
#     for i in range(len(phone_book)):
#         for j in temp[i]:
#             if str(phone_book[i]) == j[:len(phone_book[i])]:
#                 return False
#     return True

# 3차시도 이거 왜 안돼
# def solution(phone_book):
#     lenList = []
#
#     for i in phone_book:
#         lenList.append(len(i))
#
#     lenList = list(set(lenList))
#
#     dictBook = {}
#
#     for i in lenList:
#         for j in phone_book:
#             if len(j) < i:
#                 continue
#             if dictBook.get(j[:i]) == None:
#                 dictBook[j[:i]] = 1
#             else:
#                 return False
#     return True

# 성공... 근데 별로 코드 안좋아보임 startwith라는 함수도 있넹
def solution(phone_book):
    lenList = []

    for i in phone_book:
        lenList.append(len(i))

    lenList = list(set(lenList))

    dictBook = {}

    for i in lenList:
        for j in phone_book:
            if len(j) < i:
                continue
            if dictBook.get(j[:i]) == None:
                dictBook[j[:i]] = 1
            else:
                dictBook[j[:i]] = 2

    for i in phone_book:
        if dictBook.get(i) != None:
            if dictBook.get(i) == 2:
                return False

    return True

print(solution(['12','542254254254542254','4544','5422']))
