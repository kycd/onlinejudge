#/usr/local/bin/python3
# 2 star
# prime
# 26156969  12802   Gift From the Gods  Accepted    PYTH3   0.520   2021-03-05 08:10:37

import sys

m = 10 ** 6 + 1
primes = [True for x in range(m)]

for x in range(2, m):
    if primes[x] == True:
        itr = x ** 2
        while itr < m:
            primes[itr] = False
            itr += x

for inputLine in sys.stdin:
    n = int(inputLine.strip())
    print(n * 2)
    if primes[n] == True:
        if str(n) == str(n)[::-1]:
            break
