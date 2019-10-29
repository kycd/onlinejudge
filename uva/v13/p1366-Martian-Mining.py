#!/bin/python3
# 3 star dp
# 24090997  1366    Martian Mining  Accepted    PYTH3   2.560   2019-10-23 03:45:07

import sys

class MineMap:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mmap = [{} for i in range(self.n)]
        self.smap = [[ 0 for j in range(m) ] for i in range(n)]
        self.emap = [[ 0 for j in range(m) ] for i in range(n)]

    def readMap(self):
        for i in range(n):
            self.mmap[i] = list(map(int, input().strip().split(' ')))

    def preSum(self, i, j):
        if i < 0 or j < 0:
            return 0
        return self.smap[i][j]

    def countLeftPreSum(self):
        for i in range(self.n):
            for j in range(self.m):
                self.smap[i][j] = self.mmap[i][j] + self.preSum(i, j - 1)

    def countUpPreSum(self):
        for i in range(self.n):
            for j in range(self.m):
                self.smap[i][j] = self.mmap[i][j] + self.preSum(i - 1, j)

for inputLine in sys.stdin:
    n, m = list(map(int, inputLine.strip().split(' ')))
    if n == 0:
        break

    l = MineMap(n, m)
    l.readMap()
    l.countLeftPreSum()

    u = MineMap(n, m)
    u.readMap()
    u.countUpPreSum()

    for i in range(n):
        for j in range(m):
            l.emap[i][j] = l.preSum(i, j) + max(l.emap[i - 1][j], u.emap[i - 1][j])
            u.emap[i][j] = u.preSum(i, j) + max(l.emap[i][j - 1], u.emap[i][j - 1])
    print(max(l.emap[n - 1][m - 1], u.emap[n - 1][m - 1]))
