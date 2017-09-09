#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nodes = int(input())
edges = [list() for n in range(nodes)]
for i in range(nodes-1):
	x,y = map(lambda i: i-1, map(int,input().split()))
	edges[x].append(y), edges[y].append(x)

def bfs(start):
	distances, visited, queue = list(), set(), [(start,-1)]
	while queue:
		vertex,distance = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			distances.append((distance+1,vertex))
			queue.extend([(n,distance+1) for n in edges[vertex]])
	distances.sort(reverse=True)
	return distances

distance,far_node = bfs(0)[0]
max_distance,farest_node = bfs(far_node)[0]
print(max_distance)