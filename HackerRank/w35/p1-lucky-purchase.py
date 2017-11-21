#!/bin/python3

import sys
def isValidPrice(price):
    s = str(price)
    c4, c7 = [s.count("4"), s.count("7")]

    return c4 == c7 and c4 + c7 == len(s)

if __name__ == "__main__":
    n = int(input().strip())
    hasAnswer, minPrice, minPriceLaptopName = False, sys.maxsize, ""

    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]
        #print(name, value, isValidPrice(value))
        if isValidPrice(value) and value < minPrice:
           hasAnswer, minPriceLaptopName, minPrice = [True, name, value]

    print(minPriceLaptopName if hasAnswer else -1)
