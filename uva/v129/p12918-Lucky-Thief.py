#! /bin/python3
# 2 star - math
# 24119652  12918   Lucky Thief Accepted    PYTH3   0.480   2019-10-29 07:27:50

import sys

t = int(input().strip())
for caseNum in range(t):
    n, m = map(int, list(input().strip().split(' ')))
    print(int((m - n + m - 1) * n / 2))
