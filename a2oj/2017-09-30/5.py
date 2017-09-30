#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/680/B

n,a = map(int,input().split())
cities = list(map(int,input().split()))

total_criminals = len([x for x in cities if x==1])
for d in range(min(a,n-(a-1))):
    if cities[a-1-d] != cities[a-1+d]:
        total_criminals -=1

print(total_criminals)