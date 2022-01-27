def solution(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)

    number_set = set([])
    for cur in phone_book:
        if cur in number_set:
            return False
        for idx in range(0, len(cur) + 1):
            number_set.add(cur[0:idx])

    return True