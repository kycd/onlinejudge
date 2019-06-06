#!/bin/python3
# 1 star
# simulation.
# 23443654  1585    Score   Accepted    PYTH3   0.010   2019-06-06 06:34:24

import sys

n = int(input().strip())
for i in range(n):
    s = input().strip()

    scoreCurrent, scoreTotal = [0, 0]
    for x in range(len(s)):
        if s[x] == 'X':
            scoreCurrent = 0
        else:
            scoreCurrent += 1
            scoreTotal += scoreCurrent

    print(scoreTotal)
