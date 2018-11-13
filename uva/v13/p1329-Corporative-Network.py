#!/bin/python3
# 2 star union and set
# 22295045    1329    Corporative Network    Accepted    PYTH3    0.800    2018-11-13 03:43:58

class Node:
    def __init__(self, id, cost, parent):
        self.id = id
        self.cost = cost
        self.parent = parent

    def setParent(self, p):
        self.parent = p
        self.cost = abs(self.id - p.id) % 1000

    def countCost(self):
        if self.parent == None:
            return self, 0
        parent, cost = self.parent.countCost()
        self.parent = parent
        self.cost = self.cost + cost
        return parent, self.cost

    def __str__(self):
        if self.parent == None:
            return "(%d => %d, cost = %d)" % (self.id, 0, self.cost)
        return "(%d => %s, cost = %d)" % (self.id, self.parent, self.cost)

t = int(input().strip())
for caseNum in range(t):
    n = int(input().strip())
    nodes = [ Node(x, 0, None) for x in range(n + 1)]
    while 1:
        inputs = input().strip().split(' ')
        if inputs[0] == 'O':
            break

        if inputs[0] == 'E':
            x = int(inputs[1])
            nodes[x].countCost()
            print(nodes[x].cost)

        if inputs[0] == 'I':
            x, y = [int(inputs[1]), int(inputs[2])]
            nodes[x].setParent(nodes[y])
