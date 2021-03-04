#/usr/local/bin/python3
# 1 star
# xor
# 26153964  12854   Automated Checking Machine  Accepted    PYTH3   0.000   2021-03-04 09:50:30

import sys

def parse(s):
    return list(map(lambda x: True if x == '1' else False, s.strip().split(' ')))

for inputLine in sys.stdin:
    arrX = parse(inputLine)
    if len(arrX) != 5:
        break
    arrY = parse(input())

    flag = True
    for idx in range(len(arrX)):
        flag = flag and (arrX[idx] ^ arrY[idx])

    if flag == True:
        print("Y")
    else:
        print("N")
