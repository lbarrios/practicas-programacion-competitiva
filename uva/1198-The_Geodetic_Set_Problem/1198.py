#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3639

n = int(input())
adjacency_list = [list() for v in range(n+1)]
for v in range(1,n+1):
    adjacents = map(int,input().split())
    for adj in adjacents:
        a = list()
        adjacency_list[v].append(adj)

distances = [[n+1 for w in range(n+1)] for v in range(n+1)]
for v in range(1,n+1):
    distances[v][v] = 0
    for w in adjacency_list[v]:
        distances[v][w] = 1

for k in range(1,n+1):
     for j in range(1,n+1):
        for i in range(1,n+1):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]

testcases = int(input())
for t in range(testcases):
    S = list(map(int,input().split()))
    reachable = [False for v in range(n+1)]
    for s in S:
        reachable[s] = True
    for v in range(1,n+1):
        for s1 in S:
            if reachable[v]:
                break
            for s2 in S:
                if s1!=s2 and distances[s1][v] + distances[v][s2] == distances[s1][s2]:
                    reachable[v] = True
                    break
        if not reachable[v]:
            break
    print("yes" if reachable.count(True) == n else "no")