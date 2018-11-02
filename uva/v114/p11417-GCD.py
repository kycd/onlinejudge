#!/bin/python3
# 1 star
# math, array.
# 22234798    11417    GCD    Accepted    PYTH3    0.080    2018-11-02 07:34:17

import sys

def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)

arr = [0 for i in range(501)]
for i in range(2, 501):
    g = 0
    for j in range(1, i):
        g += gcd(j, i)
    arr[i] = g + arr[i - 1]

for inputLine in sys.stdin:
    n = int(inputLine.strip())
    if n == 0:
        break

    print(arr[n])
