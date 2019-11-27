#!/usr/bin/python3
# RE, input format have some problem....

import sys

class Item:
    def __init__(self, profit = -1, due = -1):
        self.profit = profit
        self.due = due

    def __repr__(self):
        return "(%s: %s)"%(self.profit, self.due)
    def __str__(self):
        return "(%d: %d)"%(self.profit, self.due)
    def __gt__(self, other):
        if self.due != other.due:
            return self.due > other.due
        else:
            return self.profit > other.profit
class Heap:
    def __init__(self, funcCompare):
        self.arr = [Item()]
        self.len = 0
        self.cmp = funcCompare

    def seek(self):
        if len(self.arr) > 1:
            return self.arr[1]
        return Item()

    def push(self, obj):
        self.arr.append(obj)
        self.build((len(self.arr) - 1) // 2, 1)

    def pop(self):
        obj = self.arr[1]
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        del self.arr[-1]
        if len(self.arr) > 1:
            self.build(1, -1)
        return obj

    def build(self, idx, direct):
        if idx <= 0:
            return
        idxP = idx // 2
        idxL = idx * 2
        idxR = idx * 2 + 1
        value = self.arr[idx]
        valueL = self.arr[idxL] if len(self.arr) > idxL else Item()
        valueR = self.arr[idxR] if len(self.arr) > idxR else Item()

        if self.cmp(valueL, value) and self.cmp(valueL, valueR):
            self.arr[idx], self.arr[idxL] = self.arr[idxL], self.arr[idx]
            idxNext = idxP if direct == 1 else idxL
            self.build(idxNext, direct)
        if self.cmp(valueR, value) and self.cmp(valueR, valueL):
            self.arr[idx], self.arr[idxR] = self.arr[idxR], self.arr[idx]
            idxNext = idxP if direct == 1 else idxR
            self.build(idxNext, direct)

def aaa(x, y):
    if x.due != y.due:
        return x.due > y.due
    else:
        return x.profit > y.profit

def bbb(x, y):
    if x.profit != y.profit:
        return x.profit > y.profit
    else:
        return x.due > y.due

def ccc(x):
    return x != ""

ans = []
for inputLine in sys.stdin:
    if inputLine.strip() == "":
        continue
    arr = list(map(int, filter(ccc, inputLine.strip().split(' '))))
#    arr = list(map(int, inputLine.strip().split(' ')))

    endingDay = 0
    warehouse = Heap(aaa)
    for x in range(1, len(arr), 2):
        warehouse.push(Item(arr[x], arr[x + 1]))
        if arr[x + 1] > endingDay:
            endingDay = arr[x + 1]
#    print(warehouse.arr)

    rack = Heap(bbb)
    maxProfit = 0
    while endingDay > 0:
#        print('-before---------------')
#        print(endingDay, "ware", warehouse.arr)
#        print(endingDay, "rack", rack.arr)
#        print('-before---------------')
        while warehouse.seek().due >= endingDay:
            rack.push(warehouse.pop())

#        print('-after---------------')
#        print(endingDay, "ware", warehouse.arr)
#        print(endingDay, "rack", rack.arr)
#        print('-after---------------')
        if rack.seek().due != -1:
            maxProfit += rack.pop().profit

        endingDay -= 1

    ans.append(maxProfit)
print(" ".join(list(map(str, ans))))
