#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem B

testcases = int(input())

def expected_value(k):
    global items
    if k==0:
        return sum(items)/len(items)
    next_expected_value = expected_value(k-1)
    expected_items = [max(i,next_expected_value) for i in items]
    return sum(expected_items)/len(expected_items)

for t in range(testcases):
    N, K = list(map(int,input().split()))
    items = list(map(int,input().split()))

    print("Case #%s: %.6f" % (t + 1, expected_value(K)))
