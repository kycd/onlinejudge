#!/usr/bin/python3
# 1 star - simulation
# 24429326  12952   Tri-du  Accepted    PYTH3   0.010   2020-01-16 10:23:17

import sys

for inputLine in sys.stdin:
    a, b = list(map(int, inputLine.strip().split(' ')))
    print(max(a, b))
