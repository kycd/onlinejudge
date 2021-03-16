#!/usr/local/bin/python3
# 2 Sstar
# set
# 26193676  10930   A-Sequence  Accepted    PYTH3   0.060   2021-03-16 03:35:28

import sys

caseNum = 1
for inputLine in sys.stdin:
    arr = inputLine.strip().split(" ")
    n = int(arr[0])
    raw = arr[1:]
    num = list(map(int, raw))

    flag = True
    sumSet = set([0, num[0]])
    for idx in range(1, n):
        if num[idx] <= num[idx - 1] or num[idx] in sumSet:
            flag = False
            break
        else:
            sumSet = set.union(sumSet, set(map(lambda x: x + num[idx], sumSet)))

    print("Case #%d: %s" % (caseNum, " ".join(raw)))
    if flag == True:
        print("This is an A-sequence.")
    else:
        print("This is not an A-sequence.")
    caseNum += 1
