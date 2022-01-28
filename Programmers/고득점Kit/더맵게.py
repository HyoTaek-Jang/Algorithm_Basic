import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while True:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return answer
        if len(scoville) == 0:
            return -1
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_1 + (min_2 * 2))
        answer += 1

    return answer