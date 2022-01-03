# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'countSubstrings' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts STRING input_str as parameter.
# #
#
# def countSubstrings(input_str):
#     # Write your code here
#     subStrings = makeSubStrings(input_str)
#
#     matchingInfo = getMatchingInfo()
#
#     answer = 0
#     for subString in subStrings:
#         length = 0
#         sumValue = 0
#
#         for cur in subString:
#             length += 1
#             sumValue += matchingInfo[cur]
#
#         if sumValue % length == 0:
#             answer += 1
#
#     return answer
#
#
# def makeSubStrings(input_str):
#     subStrings = []
#
#     inputLength = len(input_str)
#     for length in range(1, inputLength + 1):
#         for start in range(inputLength):
#             end = length + start
#             if end > inputLength:
#                 break
#             subStrings.append(input_str[start:end])
#
#     return subStrings
#
#
# def getMatchingInfo():
#     matchingInfo = {}
#
#     matchingInfo['a'] = 1
#     matchingInfo['b'] = 1
#
#     cnt = 0
#     alphaValue = 2
#     for curAlpha in "cdefghijklmnopqrstuvwxyz":
#         matchingInfo[curAlpha] = alphaValue
#
#         if cnt == 2:
#             cnt = 0
#             alphaValue += 1
#         else:
#             cnt += 1
#
#     return matchingInfo
#
#
# if __name__ == '__main__':

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#

# def countSubstrings(input_str):
#     matchingInfo = getMatchingInfo()
#
#     answer = 0
#     inputLength = len(input_str)
#     for length in range(1, inputLength + 1):
#         for start in range(inputLength):
#             end = length + start
#             if end > inputLength:
#                 break
#             subString = input_str[start:end]
#
#             length = 0
#             sumValue = 0
#             for cur in subString:
#                 length += 1
#                 sumValue += matchingInfo[cur]
#
#             if sumValue % length == 0:
#                 answer += 1
#
#     return answer
#
#
# def getMatchingInfo():
#     matchingInfo = {}
#
#     matchingInfo['a'] = 1
#     matchingInfo['b'] = 1
#
#     cnt = 0
#     alphaValue = 2
#     for curAlpha in "cdefghijklmnopqrstuvwxyz":
#         matchingInfo[curAlpha] = alphaValue
#
#         if cnt == 2:
#             cnt = 0
#             alphaValue += 1
#         else:
#             cnt += 1
#
#     return matchingInfo
#
#
# if __name__ == '__main__':

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#

# def segment(x, space):
#     # Write your code here
#     length = len(space)
#
#     maximum = 0
#     for start in range(length):
#         end = start + x
#         if end > length:
#             break
#         temp = space[start:end]
#         minValue = min(temp)
#         maximum = max(minValue, maximum)
#
#     return maximum
#
#
# if __name__ == '__main__':

from collections import deque

# from collections import deque
#
#
# def reachTheEnd(grid, maxTime):
#     maxX = len(grid)
#     maxY = len(grid[0])
#
#     timeGrid = [[1e9] * maxY for _ in range(maxX)]
#     timeGrid[0][0] = 0
#
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#
#     location = deque([])
#     location.append([0, 0, 0])
#
#     while location:
#         x, y, time = location.popleft()
#
#         for move in range(4):
#             tempX = x + dx[move]
#             tempY = y + dy[move]
#
#             if (0 > tempX or tempX == maxX or tempY == maxY or tempY < 0 or grid[tempX][tempY] == "#"):
#                 continue
#
#             if timeGrid[tempX][tempY] < 1 + time:
#                 continue
#
#             timeGrid[tempX][tempY] = 1 + time
#             location.append([tempX, tempY, 1 + time])
#
#     time = timeGrid[maxX - 1][maxY - 1]
#
#     if time <= maxTime:
#         return "Yes"
#     else:
#         return "No"
#
# reachTheEnd([['.', '.'], ['.', '.']],5)


def minimumDivision(a, b, k):
    distances = initSeparation(a, b)

    connected = len(distances)
    reduced = 0

    for start in range(connected):
        for end in range(start + 1, connected):
            if distances[end][0] - distances[start][1] <= k:
                reduced = max(reduced, end - start)

    return connected - reduced


def initSeparation(a, b):
    separation = [[[a[0], b[0]]]]
    distances = [[a[0], b[0]]]

    for idx in range(1, len(a)):
        isInto = False
        for distanceIdx in range(len(distances)):
            isInto = True
            distance = distances[distanceIdx]
            if a[idx] <= distance[0] and b[idx] >= distance[1]:
                distance[0] = a[idx]
                distance[1] = b[idx]
            elif a[idx] <= distance[0] and b[idx] <= distance[1]:
                distance[0] = a[idx]
            elif distance[0] <= a[idx] and b[idx] <= distance[1]:
                pass
            elif distance[0] <= a[idx] <= distance[1] <= b[idx]:
                distance[1] = b[idx]
            else:
                isInto = False

            if isInto:
                separation[distanceIdx].append([a[idx], b[idx]])
                break
        if not isInto:
            separation.append([[a[idx], b[idx]]])
            distances.append([a[idx], b[idx]])

    return distances