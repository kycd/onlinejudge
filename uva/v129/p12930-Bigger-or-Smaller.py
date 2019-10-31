#! /bin/python3
# 1 star string compare
# 24129087  12930   Bigger or Smaller   Accepted    PYTH3   0.000   2019-10-31 03:45:32

import sys

class obj:
    def __init__(self, s):
        self.I, self.P = s.split('.')

    def fillLeadingZero(self, len_I):
        self.I = '0' * (len_I - len(self.I)) + self.I

    def fillAppendZero(self, len_P):
        self.P = self.P + '0' * (len_P - len(self.P))

    def out(self):
        return self.I + ' ' + self.P

    def __gt__(self, other):
        return (self.I > other.I) or (self.I == other.I and self.P > other.P)
    def __eq__(self, other):
        return self.I == other.I and self.P == other.P
    def __lt__(self, other):
        return (self.I < other.I) or (self.I == other.I and self.P < other.P)

caseNum = 0
for inputLine in sys.stdin:
    caseNum += 1

    sx, sy = inputLine.strip().split(' ')
    x, y = obj(sx), obj(sy)

    len_I = max(len(x.I), len(y.I))
    len_P = max(len(x.P), len(y.P))

    x.fillLeadingZero(len_I)
    x.fillAppendZero(len_P)

    y.fillLeadingZero(len_I)
    y.fillAppendZero(len_P)

    if x > y:
        print('Case %d: Bigger' % (caseNum))
    elif x == y:
        print('Case %d: Same' % (caseNum))
    else:
        print('Case %d: Smaller' % (caseNum))

