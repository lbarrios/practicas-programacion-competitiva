#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam 2018 - Trouble Sort

def trouble_sort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L) - 2):
            if L[i] > L[i + 2]:
                done = False
                tmp = L[i]
                L[i] = L[i + 2]
                L[i + 2] = tmp


testcases = int(input())
for t in range(testcases):
    N = int(input())
    V = map(int, input().split())

    trouble_list = list(V)
    trouble_sort(trouble_list)

    ok = True
    for i in range(len(trouble_list) - 1):
        if trouble_list[i] > trouble_list[i + 1]:
            print("Case #%s: %s" % (t + 1, i))
            ok = False
            break
    if ok:
        print("Case #%s: OK" % (t + 1))
