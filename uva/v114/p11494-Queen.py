#!/bin/python3
# 1 star
# math
# 22229338    11494    Queen    Accepted    PYTH3    0.020    2018-11-01 09:35:07

import sys

for inputLine in sys.stdin:
    x1, y1, x2, y2 = inputLine.strip().split(' ')
    x1, y1, x2, y2 = [int(x1), int(y1), int(x2), int(y2)]
    if x1 == 0:
        break

    d1 = abs(x1 - x2)
    d2 = abs(y1 - y2)
    if d1 == 0 and d2 == 0:
        print(0)
    elif d1 == d2 or d1 == 0 or d2 == 0:
        print(1)
    else:
        print(2)
