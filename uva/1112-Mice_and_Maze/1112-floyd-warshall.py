#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3553

from queue import PriorityQueue

testcases = int(input())
for t in range(testcases):
    input() # there is an empty line between testcases
    N,E,T,M = int(input()),int(input()),int(input()),int(input())
    connections = [list() for b in range(N+1)]
    for m in range(M):
        a, b, time_units = map(int,input().split())
        connections[b].append((time_units,a))
    # Floyd-Warshall, starting from E
    distances = [[T+1 for a in range(N+1)] for b in range(N+1)]
    for v in range(1,N+1):
        distances[v][v] = 0
        for (d,e) in connections[v]:
            distances[v][e] = d
    for k in range(1,N+1):
        for j in range(1, N + 1):
            for i in range(1, N + 1):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    total = sum([1 for d in distances[E] if d<=T])
    print(total)
    # because of strange output format, we need a new line if this is NOT the last testcase
    if(t < testcases-1):
        print()