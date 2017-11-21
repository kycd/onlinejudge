#!/bin/python3

import sys

def fillMatrixHorizontal(matrix, n, p):
    for i in range(p + 1, n):
        matrix[p][i] = matrix[p][i-1] - 1
    return matrix

def fillMatrixVertical(matrix, n, p):
    for i in range(p + 1, n):
        matrix[i][p] = matrix[i-1][p] - 1
    return matrix

def tripleRecursion(n, m, k):
    matrix = [[0 for x in range(n)] for y in range(n)]
    matrix[0][0] = m;
    matrix = fillMatrixHorizontal(matrix, n, 0)
    matrix = fillMatrixVertical(matrix, n, 0)

    for i in range(1, n):
        matrix[i][i] = matrix[i-1][i-1] + k
        matrix = fillMatrixHorizontal(matrix, n, i)
        matrix = fillMatrixVertical(matrix, n, i)

    return matrix

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    matrix = tripleRecursion(n, m, k)
    for i in range(n):
        print(" ".join(str(x) for x in matrix[i]))
