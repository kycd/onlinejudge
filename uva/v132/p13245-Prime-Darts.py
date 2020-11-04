#!/usr/local/python3
# 3 star dp
# 25673071  13245   Prime Darts Accepted    PYTH3   0.370   2020-10-30 06:27:14

import sys

# prime table
primes = [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523]

# build all answer table
lx, ly = 5000, 100
ans = [[x for y in range(ly + 1)] for x in range(lx + 1)]
for y in range(1, ly + 1):
    for x in range(1, lx + 1):
        ans[x][y] = ans[x][y-1]
        if x >= primes[y]:
            ans[x][y] = min(ans[x - primes[y]][y] + 1, ans[x][y-1])

t = int(input().strip())
for i in range(t):
    n, q = list(map(int, input().strip().split(' ')))
    print(ans[q][n])
