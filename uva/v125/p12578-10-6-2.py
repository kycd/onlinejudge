#!/bin/python3
# 1 star
# math
# 20571230    12578    10:6:2    Accepted    PYTH3    0.020    2018-01-05 10:07:36

import sys
import math

def countCircleArea(length):
    r = length / 5
    return r * r * math.acos(-1)

def countRectangleArea(length):
    return length * 0.6 * length - countCircleArea(length)

t = int(input().strip())
for i in range(t):
    length = int(input().strip())

    print("{0:.2f} {1:.2f}".format(countCircleArea(length), countRectangleArea(length)))
