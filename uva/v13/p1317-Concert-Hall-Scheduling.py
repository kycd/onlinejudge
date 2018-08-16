#!/bin/python3
# TLE

import sys

m = 366
class Application():
    def __init__(self, i, j, price):
        self.fromDay = i
        self.toDay = j
        self.price = price
    def __lt__(self, other):
        return self.toDay < other.toDay

class Contract():
    def __init__(self, ap1, ap2, price):
        self.ap1 = ap1
        self.ap2 = ap2
        self.price = price

class Blueprint():
    def __init__(self):
        self.contracts = [{} for x in range(m)]
        self.contracts[0][0] = 0
        self.maxProfit = 0
    def handle(self, x):
        tmpDict = [{} for x in range(m)]
        curPlan = self.contracts
        for i in range(m):
            for j in curPlan[i].keys():
                if i < x.fromDay and curPlan[x.toDay].get(j, -1) < curPlan[i][j] + x.price :
                    tmpDict[x.toDay][j] = curPlan[i][j] + x.price
                    if self.maxProfit < tmpDict[x.toDay][j]:
                        self.maxProfit = tmpDict[x.toDay][j]
                if j < x.fromDay and curPlan[i].get(x.toDay, -1) < curPlan[i][j] + x.price :
                    tmpDict[i][x.toDay] = curPlan[i][j] + x.price
                    if self.maxProfit < tmpDict[i][x.toDay]:
                        self.maxProfit = tmpDict[i][x.toDay]
        for i in range(m):
            curPlan[i].update(tmpDict[i])

for inputLine in sys.stdin:
    n = int(inputLine.strip())
    if n == 0:
        break

    applications = []
    for i in range(n):
        i, j, price = input().strip().split(' ')
        applications.append(Application(int(i), int(j), int(price)))
    applications = sorted(applications)
    
    plan = Blueprint()
    for application in applications:
        plan.handle(application)
    print(plan.maxProfit)
