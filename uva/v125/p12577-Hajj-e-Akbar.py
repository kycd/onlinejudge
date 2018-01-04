#!/bin/python3
# 1 star
# if-else =  =.
# 20565993    12577    Hajj-e-Akbar    Accepted    PYTH3    0.020    2018-01-04 03:59:44

import sys

caseNum = 0;
for inputLine in sys.stdin:
    str = inputLine.strip().split(' ')[0]

    if str == '*':
        break;

    caseNum += 1;
    if str == 'Hajj':
        print('Case {0}: Hajj-e-Akbar'.format(caseNum))
    else:
        print('Case {0}: Hajj-e-Asghar'.format(caseNum))
