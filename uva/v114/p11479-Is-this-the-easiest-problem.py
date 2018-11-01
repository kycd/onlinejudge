#!/bin/python3
# 1 star
# 22229505    11479    Is this the easiest problem?    Accepted    PYTH3    0.000    2018-11-01 10:23:49

t = int(input().strip())

for i in range(t):
    inputLine = input().strip()

    a, b, c = inputLine.split(' ')
    a, b, c = sorted([int(a), int(b), int(c)])

    if c - b >= a or a <= 0:
        print("Case {0:d}: Invalid".format(i + 1))
    elif a == b and b == c:
        print("Case {0:d}: Equilateral".format(i + 1))
    elif a == b or b == c:
        print("Case {0:d}: Isosceles".format(i + 1))
    else:
        print("Case {0:d}: Scalene".format(i + 1))
