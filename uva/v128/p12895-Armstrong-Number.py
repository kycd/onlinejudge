#/usr/local/bin/python3
# 1 star
# math
# 26153351  12895   Armstrong Number    Accepted    PYTH3   0.010   2021-03-04 06:27:15

t = int(input().strip())

for i in range(t):
    n = input().strip()
    arr = list(map(int, list(n)))
    p = len(n)

    if sum(map(lambda x: x ** p, arr)) == int(n):
        print("Armstrong")
    else:
        print("Not Armstrong")
