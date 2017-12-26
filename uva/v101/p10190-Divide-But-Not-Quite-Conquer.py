#!/bin/python3
# 1 star
# simulation.
# 20536448    10190    Divide, But Not Quite Conquer!    Accepted    PYTH3    0.010    2017-12-26 10:02:03

import sys

for inputLine in sys.stdin:
    n, k = inputLine.strip().split(' ')
    n, k = [int(n), int(k)]

    if k <= 1 or n <= 1:
        print('Boring!')
    else:
        arr = []
        flag = True
        while n > 1 and flag:
            if n % k != 0:
                flag = False
                break
            arr.append(n)
            n = int(n / k)
        arr.append(1)

        if flag == True:
            print(*arr)
        else:
            print('Boring!')
