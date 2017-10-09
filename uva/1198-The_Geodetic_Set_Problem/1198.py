#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3639

n = int(input())
adjacency_list = [list() for v in range(n)]
for v in range(n):
    adjacents = map(int,input().split())
    for adj in adjacents:
        a = list()
        adjacency_list[v].append(adj)

def get_reachables_from(from_node, current_node, current_path):
    global reachables_from

reachables_from = [set() for v in range(n)]
for v in range(n):
    get_reachables_from(v)