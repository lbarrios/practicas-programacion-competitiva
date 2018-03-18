#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem B

testcases = int(input())

for t in range(testcases):
    N, K = list(map(int,input().split()))
    items = list(map(int,input().split()))

    print("Case #%s: %s %s" % (t + 1, N, K))
