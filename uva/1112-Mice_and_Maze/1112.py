#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3553

from queue import PriorityQueue

testcases = int(input())
for t in range(testcases):
    input() # there is an empty line between testcases
    N,E,T,M = int(input()),int(input()),int(input()),int(input())
    connections = [list() for b in range(N+1)]
    distances_from_E = [T+1 for a in range(N+1)]
    distances_from_E[E] = 0
    for m in range(M):
        a, b, time_units = map(int,input().split())
        connections[b].append((time_units,a))
    # Dijkstra, starting from E
    pending_nodes = PriorityQueue()
    pending_nodes.put((0,E))
    while not pending_nodes.empty():
        (priority, current_node) = pending_nodes.get()
        for (d,node) in connections[current_node]:
            if distances_from_E[current_node] + d < distances_from_E[node]:
                distances_from_E[node] = distances_from_E[current_node] + d
                pending_nodes.put((d,node))
    total = sum([1 for d in distances_from_E if d<=T])
    print(total)
    # because of strange output format, we need a new line if this is NOT the last testcase
    if(t < testcases-1):
        print()