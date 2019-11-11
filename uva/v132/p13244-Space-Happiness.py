#!/usr/bin/python
# 1 star math
# 24177452  13244   Space Happiness Accepted    PYTH3   0.000   2019-11-11 03:50:50

def countCost(speed):
    return (speed * speed + 1) // 2

n = int(input().strip())
for i in range(n):
    s = int(input().strip())
    print(countCost(s))
