#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem A

testcases = int(input())


def check_all_even(N):
    for d in range(len(N)):
        if int(N[d]) % 2 == 1:
            return False
    return True


for t in range(testcases):
    N = input()
    if check_all_even(N):
        print("Case #%s: 0" % (t + 1,))
        continue

    N_add = int(N)
    adds=0
    N_sub = int(N)
    subs=0

    while not check_all_even(str(N_add)):
        N_add+=1
        adds+=1

    while not check_all_even(str(N_sub)):
        N_sub-=1
        subs+=1
    print("Case #%s: %s" % (t + 1, min(adds, subs)))
