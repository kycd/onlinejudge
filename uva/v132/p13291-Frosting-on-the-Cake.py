#!/usr/local/bin/python3
# 1 star math
# 25622733  13291   Frosting on the Cake    Accepted    PYTH3   0.580   2020-10-16 09:36:14

import sys

for inputLine in sys.stdin:
    n = int(inputLine.strip())
    partionA = list(map(int, input().strip().split(' ')))
    partionB = list(map(int, input().strip().split(' ')))

    groupA = [0, 0, 0]
    groupB = [0, 0, 0]
    for i in range(n):
        groupA[i % 3] += partionA[i]
        groupB[i % 3] += partionB[i]

    group = [0, 0, 0]
    group[0] += groupA[0] * groupB[0]
    group[0] += groupA[1] * groupB[2]
    group[0] += groupA[2] * groupB[1]

    group[1] += groupA[0] * groupB[1]
    group[1] += groupA[1] * groupB[0]
    group[1] += groupA[2] * groupB[2]

    group[2] += groupA[0] * groupB[2]
    group[2] += groupA[1] * groupB[1]
    group[2] += groupA[2] * groupB[0]

    print("%d %d %d" % (group[1], group[2], group[0]))
