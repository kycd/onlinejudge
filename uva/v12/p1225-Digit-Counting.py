#!/bin/python3
# 1 star, simulation
# 24156846  1225    Digit Counting  Accepted    PYTH3   0.050   2019-11-06 10:02:46

class Digit:
    def __init__(self, n):
        self.digits = [0 for x in range(10)]
        self.number = n

    def countDigit(self):
        num = str(self.number)
        for i in range(len(num)):
            self.digits[int(num[i])] += 1
        return self

    def toString(self):
        return str.join(" ", list(map(str, self.digits)))

    def __add__(self, other):
        self.digits = list(map(lambda x, y: x + y, self.digits, other.digits))
        return self

def init(m):
    arr = []
    for i in range(m):
        arr.append(Digit(i).countDigit())

    for i in range(2, m):
        arr[i] = arr[i] + arr[i-1]

    return arr

arr = init(10000)
caseNum = int(input().strip())
for i in range(caseNum):
    n = int(input().strip())
    print(arr[n].toString())
