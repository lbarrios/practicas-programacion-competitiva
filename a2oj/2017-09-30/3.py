#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/427/A

n = int(input())
timeline = map(int, input().split())

polices = 0
untreated = 0
for event in timeline:
    if event > 0:
        polices += event
    else:
        if polices > 0:
            polices -= 1
        else:
            untreated += 1

print(untreated)
