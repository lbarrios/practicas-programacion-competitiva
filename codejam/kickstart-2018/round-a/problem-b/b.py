#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem B
import functools

for t in range(int(input())):
    N, K, Vs = list(map(int, input().split()))+[list(map(int, input().split()))]
    print("Case #%s: %.6f" % (t + 1, functools.reduce(lambda x, y: sum([max(i, x) * p for (i, p) in [(i, Vs.count(i) / len(Vs)) for i in set(Vs)]]), range(K), sum(Vs) / len(Vs))))