# import collections
# 
# 
# def solution(bridge_length, weight, truck_weights):
#     temp = collections.deque([0] * bridge_length)
#     truck_weights.sort()
#     trucks = collections.deque(truck_weights)
#     check = True
#     answer = 0
# 
#     while trucks or sum(temp) != 0:
#         answer += 1
#         temp.popleft()
# 
#         if sum(temp) >= weight or not trucks:
#             temp.append(0)
#             continue
# 
#         if check:
#             curTruck = trucks.pop()
#             if sum(temp) + curTruck > weight:
#                 trucks.append(curTruck)
#                 temp.append(0)
#                 continue
#             temp.append(curTruck)
#             check = False
#         else:
#             curTruck = trucks.popleft()
#             if sum(temp) + curTruck > weight:
#                 trucks.appendleft(curTruck)
#                 temp.append(0)
#                 continue
#             temp.append(curTruck)
#             check = True
# 
# 
#     return answer
# 
# print(solution(2,10,[7,4,5,6]))

def solution(prices):
    time = []
    temp = [-1] * len(prices)

    for i in range(len(prices)):

        for k in range(len(time)):
            time[k] = time[k] + 1

        for j in range(i):
            if prices[i] < prices[j]:
                temp[j] = time[j]

        time.append(0)

    for k in range(len(temp)):
        if temp[k] == -1: temp[k] = time[k]

    return temp

solution([1,2,3,2,3])