def solution(phone_book):
    temp = {}
    setBook = set(phone_book)
    for i in range(len(setBook)):
        value = set([phone_book[i]])
        temp[i] = setBook - value

    for i in range(len(phone_book)):
        for j in temp[i]:
            if str(phone_book[i]) in str(j):
                return False
    return True

solution([1,5,6,234])