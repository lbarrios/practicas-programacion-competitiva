#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nodes = int(input())
edges = [list() for n in range(nodes)]
visited = [False for n in range(nodes)]
for i in range(nodes-1):
	x,y = map(lambda i: i-1, map(int,input().split()))
	edges[x].append(y)
	edges[y].append(x)

max_paths = [list() for n in range(nodes)]

def travel(node, count):
	visited[node] = True
	for n2 in edges[node]:
		if not visited[n2]:
			t = travel(n2, count+1)
			print("travel for nodes %s %s = %s"%(node,n2,t))
			max_paths[node].append(t)
			print(max_paths)
	return count


visited[0] = True
for n in edges[0]:
	max_paths[0].append(travel(n, 1))

max_total = 0
for n in range(nodes):
	max_paths[n].sort()
	if len(max_paths[n])>1:
		max_total = max(max_total, max_paths[n][-1]+max_paths[n][-2])
	elif len(max_paths[n])>0:
		max_total = max(max_total, max_paths[n][0])

print(max_paths)

print(max_total)