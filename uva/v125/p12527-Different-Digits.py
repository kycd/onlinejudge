#!/bin/python3
# 1 star
# math
# 20618921    12527    Different Digits    Accepted    PYTH3    0.060    2018-01-17 10:18:18

import sys
import math

def countDigits(num):
    return int(math.log10(num)) + 1

def countUniqueDigits(num):
    arr = [0 for x in range(10)]
    x = num
    while(x > 0):
        arr[int(x % 10)] = 1
        x = int(x / 10)
    return sum(arr)

isUniqueDigits = [0 for x in range(5001)]
for x in range(1, 5001):
    if (countDigits(x) == countUniqueDigits(x)):
        isUniqueDigits[x] = 1

for inputLine in sys.stdin:
    n, m = inputLine.strip().split(' ')
    n, m = [int(n), int(m)]

    print(sum(isUniqueDigits[n : m + 1]))
