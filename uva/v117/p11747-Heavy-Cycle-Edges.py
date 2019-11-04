#!/bin/python3
# 2~3 star
# MST
# 24147000  11747   Heavy Cycle Edges   Accepted    PYTH3   0.030   2019-11-04 08:43:37

import sys

def getMapSize():
    return map(int, input().strip().split(' '))

def getEdge():
    x, y, w = list(map(int, input().strip().split(' ')))
    return Edge(x, y, w)

class Edge:
    def __init__(self, x, y, w):
        self.nodeX = x
        self.nodeY = y
        self.weight = w

class Graph:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.edges = []
        self.leftEdges = []

    def getEdges(self, m):
        for i in range(m):
            self.edges.append(getEdge())
        self.edges = sorted(self.edges, key=lambda x: x.weight)

    def getRoot(self, node):
        if self.parents[node] == node:
            return node

        root = self.getRoot(self.parents[node])
        self.parents[node] = root
        return root

    def union(self):
        for edge in self.edges:
            rootX = self.getRoot(edge.nodeX)
            rootY = self.getRoot(edge.nodeY)
            if rootX != rootY:
                self.parents[rootX] = rootY
            else:
                self.leftEdges.append(str(edge.weight))

while 1:
    n, m = getMapSize()
    if n == 0:
        break

    graph = Graph(n)
    graph.getEdges(m)
    graph.union()

    if len(graph.leftEdges) == 0:
        print("forest")
    else:
        print(" ".join(graph.leftEdges))

