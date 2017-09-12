#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/567/C/

n, k = map(int, input().split())
s = list(map(int, input().split()))
ss = list()
ss.append(list(s))
ss.append(list(s))
ss.append(list(s))


def check_geometric(a, b, c):
    global k
    return b == a * k and c == a * k * k

def dp(pos)

total = 0

# for i1 in range(0, len(s) - 2):
#     for i2 in range(i1 + 1, len(s) - 1):
#         for i3 in range(i2 + 1, len(s)):
#             total += 1 if check_geometric(s[i1], s[i2], s[i3]) else 0

for j in range(3):
    kj = k**j
    for i in range(0, len(s) - 1):
        ss[j][i] = i/kj

s.sort()

print(total)
