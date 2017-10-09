#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3639

# Input reading
n = int(input())
adjacency_list = [list() for v in range(n + 1)]
for v in range(1, n + 1):
    adjacents = map(int, input().split())
    for adj in adjacents:
        a = list()
        adjacency_list[v].append(adj)

# Floyd Warshall
distances = [[n + 1 for w in range(n + 1)] for v in range(n + 1)]
for v in range(1, n + 1):
    distances[v][v] = 0
    for w in adjacency_list[v]:
        distances[v][w] = 1
for k in range(1, n + 1):
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]


def is_in_minimum_path(v, s1, s2):
    global distances
    return distances[s1][v] + distances[v][s2] == distances[s1][s2]


# Answering the testcases
testcases = int(input())
for t in range(testcases):
    S = list(map(int, input().split()))
    reachables = [[is_in_minimum_path(v, s1, s2) for s1 in S for s2 in S].count(True) >= 1 for v in
                  range(1, n + 1)]
    print("yes" if reachables.count(True) == n else "no")
