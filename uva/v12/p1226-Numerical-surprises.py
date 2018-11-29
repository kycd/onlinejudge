#!/bin/python3
# 1 star if using python or java. Big Integer
# 22365141    1226    Numerical surprises    Accepted    PYTH3    0.000    2018-11-28 10:32:28

import sys

caseTotal = int(input().strip())
for caseNum in range(caseTotal):
    n = int(input().strip())
    p = int(input().strip())
    print(p % n)
