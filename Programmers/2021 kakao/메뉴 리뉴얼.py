from itertools import combinations

def solution(orders, course):
    answer = []
    _dict = {}

    for c in course:
        _dict[c] = {}
        for order in orders:
            if len(order) >= c:
                idx = combinations(order, c)

                for combi in idx:
                    sortCombi = list(combi)
                    sortCombi.sort()

                    temp = "".join(sortCombi)
                    if temp in _dict[c]:
                        _dict[c][temp] += 1
                    else:
                        _dict[c][temp] = 0
        print(_dict[c])

        rank = sorted(_dict[c].items(), key=lambda x: x[1], reverse=True)
        tempRank = 1
        while len(rank) > 0 and rank[0][1] >= tempRank:
            popRank = rank.pop(0)
            answer.append(popRank[0])
            tempRank = popRank[1]

        answer.sort()

    return answer