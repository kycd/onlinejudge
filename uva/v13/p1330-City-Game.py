#! /usr/bin/python3
# 3 star dp
# Runtime error.

import sys

k = int(input().strip())
for inputLine in sys.stdin:
    if inputLine.strip() == '':
        continue
    m, n = list(map(int, inputLine.strip().split(' ')))
    maps = [['R' for i in range(n + 1)]]
    for x in range(m):
        row = input().strip().split(' ')
        row.insert(0, 'R')
        maps.append(row)

    width = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if maps[x][y] == 'F':
                width[x][y] = width[x][y - 1] + 1

    maxArea = 0
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if maps[x][y] == 'F':
                maxWidth = width[x][y]
                for z in range(x, 0, -1):
                    if maps[z][y] == 'R':
                        break
                    maxWidth = min(maxWidth, width[z][y])
                    area = maxWidth * (x - z + 1)
                    if maxArea < area:
                        maxArea = area
    print(maxArea * 3)
