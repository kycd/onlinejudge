#!/usr/bin/python3
# 1 star - greedy
# 25125501  12955   Factorial   Accepted    PYTH3   0.010   2020-06-10 07:25:32

import sys

def divide(n, f):
    ans = 0

    idx = 0
    while n > 0:
        if n >= f[idx]:
            n -= f[idx]
            ans += 1
        else:
            idx += 1

    return ans

def generateFactorial():
    f = [1]
    x = 2
    while f[-1] < 10e5:
        f.append(f[-1] * x)
        x += 1
    f.reverse()
    return f

f = generateFactorial()
for inputLine in sys.stdin:
    n = int(inputLine.strip())
    print(divide(n, f))
