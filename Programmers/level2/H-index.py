def solution(citations):
    _hash = {}

    for i in citations:
        for j in range(i + 1):
            if j in _hash:
                _hash[j] += 1
            else:
                _hash[j] = 1

    i = 1
    key = list(_hash.keys())
    while True:
        if key[-i] <= _hash[key[-i]]:
            return key[-i]
        i += 1