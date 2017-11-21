#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    matrix = [[0 for x in range(n + 1)] for y in range(n + 1)]
    matrix[0][0] = m - k;

    for i in range(1, n + 1):
        matrix[i][i] = matrix[i - 1][i - 1] + k
        for j in range(i + 1, n + 1):
            matrix[i][j] = matrix[i][j - 1] - 1
            matrix[j][i] = matrix[j - 1][i] - 1

    return matrix

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    matrix = tripleRecursion(n, m, k)

    for i in range(1, n + 1):
        print(" ".join(str(matrix[i][x]) for x in range(1, n + 1)))
