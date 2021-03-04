#/usr/local/bin/python3

t = int(input().strip())

for i in range(t):
    n = input().strip()
    arr = list(map(int, list(n)))
    p = len(n)

    if sum(map(lambda x: x ** p, arr)) == int(n):
        print("Armstrong")
    else:
        print("Not Armstrong")
