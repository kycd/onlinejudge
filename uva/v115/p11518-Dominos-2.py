#!/bin/python3
# 2 star
# bfs
# 29253198  11518   Dominos 2   Accepted    PYTH3   1.180   2024-03-04 10:40:19

t = int(input())
for _ in range(t):
	n, m, l = list(map(int, input().split(' ')))

	maps = [[] for _ in range(n + 1)]
	for _ in range(m):
		x, y = list(map(int, input().split(' ')))
		maps[x].append(y)

	q = []
	for _ in range(l):
		q.append(int(input()))

	v = [0 for _ in range(n + 1)]
	for x in q:
		v[x] = 1

	for x in q:
		for y in maps[x]:
			if v[y] == 0:
				v[y] = 1
				q.append(y)
	print(v.count(1))
