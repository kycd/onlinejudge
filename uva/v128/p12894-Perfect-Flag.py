#/usr/local/bin/python3
# 1 star
# math
# 26767265  12894   Perfect Flag    Accepted    PYTH3   0.010   2021-09-13 03:22:59

n = int(input())

for i in range(n):
    [x0, y0, x1, y1, cx, cy, cr] = list(map(int, input().strip().split(" ")))
    #print(x0, y0, x1, y1, cx, cy, cr)
    length = x1 - x0
    width = y1 - y0

#    print(length, width)
    # check length width ratio is 10:6
    if length * 3 != width * 5:
        print("NO")
        continue

    # check length radius ratio is 2:1
    if length != cr * 5:
        print("NO")
        continue

    # check circle center position at 0.45x, 0.5y of flag
    if x0 + length * 0.45 != cx:
        print("NO")
        continue
    if y0 + width * 0.5 != cy:
        print("NO")
        continue

    print("YES")
