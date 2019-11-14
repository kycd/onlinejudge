#!/bin/python3
# 3 star dp
# 24183736  1366    Martian Mining  Accepted    PYTH3   2.210   2019-11-12 10:28:52

import sys

class MineMap:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mineMap = [{} for i in range(self.n)]
        self.sumMap = [[ 0 for j in range(m) ] for i in range(n)]

    def read(self):
        for i in range(self.n):
            self.mineMap[i] = list(map(int, input().strip().split(' ')))

    def fetch(self, i, j):
        if i < 0 or j < 0:
            return 0
        return self.sumMap[i][j]
    
    def countYeyePreSum(self):
        for i in range(self.n):
            for j in range(self.m):
                self.sumMap[i][j] = self.mineMap[i][j] + self.fetch(i, j - 1)

    def countBlogPreSum(self):
        for i in range(self.n):
            for j in range(self.m):
                self.sumMap[i][j] = self.mineMap[i][j] + self.fetch(i - 1, j)

class MiningStrategy:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.Optimize = MineMap(n, m)
        self.yeyeMap = MineMap(n, m)
        self.blogMap = MineMap(n, m)

    def readYeyeMap(self):
        self.yeyeMap.read()
        self.yeyeMap.countYeyePreSum()

    def readBlogMap(self):
        self.blogMap.read()
        self.blogMap.countBlogPreSum()

    def count(self):
        for i in range(self.n):
            for j in range(self.m):
                self.Optimize.sumMap[i][j] = max(self.yeyeMap.fetch(i, j) + self.Optimize.fetch(i - 1, j), self.blogMap.fetch(i, j) + self.Optimize.fetch(i, j - 1))

for inputLine in sys.stdin:
    n, m = list(map(int, inputLine.strip().split(' ')))
    if n == 0:
        break

    strategy = MiningStrategy(n, m)
    strategy.readYeyeMap()
    strategy.readBlogMap()
    strategy.count()

    print(strategy.sumMap.fetch(n - 1, m - 1))
