#!/bin/python3
# 1 star
# math
# 22234927    11455    Behold my quadrangle    Accepted    PYTH3    0.010    2018-11-02 08:08:56

import sys

t = int(input().strip())
for caseNum in range(t):
    a, b, c, d = input().strip().split(' ')
    a, b, c, d = sorted([int(a), int(b), int(c), int(d)])

    if a == d:
        print("square")
    elif a == b and c == d:
        print("rectangle")
    elif a + b + c > d:
        print("quadrangle")
    else:
        print("banana")
