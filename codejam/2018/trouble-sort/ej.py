#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam 2018 - Trouble Sort

testcases = int(input())
for t in range(testcases):
    N = int(input())
    V = input().split()

    list_even = [int(V[i]) for i in range(0, len(V), 2)]
    list_odd = [int(V[i]) for i in range(1, len(V), 2)]

    list_even.sort()
    list_odd.sort()

    list_final = [list_even[i//2] if i%2==0 else list_odd[i//2] for i in range(len(list_even) + len(list_odd))]

    ok = True
    for i in range(len(list_final) - 1):
        if list_final[i] > list_final[i + 1]:
            print("Case #%s: %s" % (t + 1, i))
            ok = False
            break

    if ok:
        print("Case #%s: OK" % (t + 1))
