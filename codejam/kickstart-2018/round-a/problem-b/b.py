#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem B

testcases = int(input())
for t in range(testcases):
    N, K = list(map(int, input().split()))
    items = list(map(int, input().split()))
    items_with_p = [(i, items.count(i) / len(items)) for i in set(items)]

    expected_value = [sum(items) / len(items)] + [0] * K
    for k in range(1, K + 1):
        next_expected_value = expected_value[k - 1]
        for (i, p) in items_with_p:
            expected_value[k] += max(i, next_expected_value) * p

    print("Case #%s: %.6f" % (t + 1, expected_value[K]))
