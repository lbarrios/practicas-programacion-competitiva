#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem B

def expected_value(k):
    if k not in _expected_value:
        _expected_value[k] = 0
        next_expected_value = expected_value(k - 1)
        for (i, p) in items_with_p:
            _expected_value[k] += max(i, next_expected_value) * p
    return _expected_value[k]


testcases = int(input())
for t in range(testcases):
    N, K = list(map(int, input().split()))
    items = list(map(int, input().split()))
    items_with_p = [(i, items.count(i) / len(items)) for i in set(items)]
    _expected_value = {0: sum(items) / len(items)}

    for k in range(K):
        expected_value(k)

    print("Case #%s: %.6f" % (t + 1, expected_value(K)))
