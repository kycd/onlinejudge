#!/usr/local/bin/python3
# 1 star math
# 25585264  13275   Leap Birthdays  Accepted    PYTH3   0.010   2020-10-07 04:02:15

import sys

def cntLeapYear(n):
    return int(n / 4) - int(n / 100) + int(n / 400)

n = int(input().strip())
for caseNum in range(n):
    date, month, year, queryYear = list(map(int, input().strip().split()))
    
    ans = 0
    if month == 2 and date == 29:
        ans = cntLeapYear(queryYear) - cntLeapYear(year)
    else:
        ans = queryYear - year
    print("Case %d: %d" % (caseNum + 1, ans))
