#!/bin/python3
# 3 star
# binary search.
# 25099298  11516   WiFi    Accepted    PYTH3   0.560   2020-06-03 07:10:52

def guess(houses, n, preferRange):
    cnt, coverdSide = 0, 0
    for i in range(len(houses)):
        if houses[i] > coverdSide:
            cnt += 1
            coverdSide = houses[i] + preferRange

    return cnt <= n

caseTotal = int(input().strip())
for caseNum in range(caseTotal):
    n, m = list(map(int, input().strip().split(' ')))

    houses = []
    for x in range(m):
        houses.append(int(input().strip()))
    houses = sorted(houses)

    rangeMin, rangeMax, ans = 0, houses[-1], houses[-1]
    while rangeMin <= rangeMax:
        mid = (rangeMin + rangeMax) // 2
        if guess(houses, n, mid) == True:
            ans = mid
            rangeMax = mid - 1
        else:
            rangeMin = mid + 1

    print("%.1f" % (ans / 2))
