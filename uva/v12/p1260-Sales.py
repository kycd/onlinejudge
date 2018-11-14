#!/bin/python3
# 2 star insertion sort.
# 22299458    1260    Sales    Accepted    PYTH3    1.650    2018-11-14 03:41:00

import sys

t = int(input().strip())
for caseNum in range(t):
    n = int(input().strip()) + 1
    arr = list(map(int, input().strip().split(' ')))
    arr.insert(0, 0)

    ans = 0
    for i in range(1, n):
        x = arr[i]
        for j in range(i, 0, -1):
            if x >= arr[j -1]:
                arr[j] = x
                ans += (j - 1)
                break
            else:
                arr[j] = arr[j-1]

    print(ans)
