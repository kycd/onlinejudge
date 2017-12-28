#!/bin/python3
# 1 star (2 star if handle big-integer self.)
# 20543914    530    Binomial Showdown    Accepted    PYTH3    0.010    2017-12-28 09:46:52

import sys

for inputLine in sys.stdin:
    n, k = inputLine.strip().split(' ')
    n, k = [int(n), int(k)]
    if n == 0:
        break;

    if k > n / 2:
        k = n - k

    answer = 1
    for x in range(k):
        answer *= (n-x)
    for x in range(2, k + 1):
        answer /= x
    print(int(answer))
