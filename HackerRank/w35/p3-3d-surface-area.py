#!/bin/python3

import sys

def surfaceArea(A, H, W):
    ans = 2 * H * W
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            ans += max(A[i][j] - A[i-1][j], 0)
            ans += max(A[i][j] - A[i][j-1], 0)
            ans += max(A[i][j] - A[i+1][j], 0)
            ans += max(A[i][j] - A[i][j+1], 0)
    return ans

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = [[0 for x in range(W + 2)]]
    for A_i in range(H):
        A_t = [0] + [int(A_temp) for A_temp in input().strip().split(' ')] + [0]
        A.append(A_t)
    A.append([0 for x in range(W + 2)])
    result = surfaceArea(A, H, W)
    print(result)

