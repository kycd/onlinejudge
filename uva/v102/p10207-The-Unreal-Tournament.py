#!/bin/python3
# 3 star.
# DP, Big-Integer
# 20543758    10207    The Unreal Tournament    Accepted    PYTH3    5.310    2017-12-28 09:01:23

import sys

# times array is same for each testcase.
MAX_TIMES = 1001
times = [[1 for x in range(MAX_TIMES)] for y in range(MAX_TIMES)]
for x in range(1, MAX_TIMES):
    for y in range(1, MAX_TIMES):
        times[x][y] = times[x-1][y] + times[x][y-1] + 1

isFirstCase = True
for inputLine in sys.stdin:
    p, n = inputLine.strip().split(' ')
    p, n = [float(p), int(n)]
    if n == 0:
        break

    if isFirstCase:
        isFirstCase = False
    else:
        print()
    
    # winrate is same for each query in one testcase
    winrate = [[-1 for x in range(MAX_TIMES)] for y in range(MAX_TIMES)]
    for x in range(1, MAX_TIMES):
        winrate[x][0], winrate[0][x] = [0, 1]

    for x in range(1, MAX_TIMES):
        for y in range(1, MAX_TIMES):
            winrate[x][y] = p*winrate[x-1][y] + (1-p)*winrate[x][y-1]

    for i in range(n):
        i, j = input().strip().split(' ')
        i, j = [int(i), int(j)]
        print("{0:.5f}".format(winrate[i][j]))
        print(times[i][j] - 1)

