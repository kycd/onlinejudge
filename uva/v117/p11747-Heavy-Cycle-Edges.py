#!/bin/python3
# 2 star
# MST
# 23493030  11747   Heavy Cycle Edges   Accepted    PYTH3   0.030   2019-06-20 06:54:51

import sys

def getSequenceInt():
    arr = []
    for x in input().strip().split(' '):
        arr.append(int(x))
    return arr

def getParent(x):
    if parents[x] == x:
        return x
    else:
        root = getParent(parents[x])
        parents[x] = root
        return root

parents = []
while 1:
    n, m = getSequenceInt()
    if n == 0:
        break

    edges = []
    parents = [x for x in range(n)]
    edges = []
    for i in range(m):
        edges.append(getSequenceInt())
    edges = sorted(edges, key=lambda x: x[2])

    ans = []
    for edge in edges:
        rootX = getParent(edge[0])
        rootY = getParent(edge[1])
        if rootX != rootY:
            parents[rootX] = rootY
        else:
            ans.append(edge[2])
    ans = list(map((lambda x: str(x)),  ans))
    if len(ans) == 0:
        print("forest")
    else:
        print(" ".join(ans))
