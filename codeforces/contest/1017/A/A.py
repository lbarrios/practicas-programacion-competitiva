#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ranks=list()
students = int(input())
for id in range(students):
    scores = map(int, input().split())
    ranks.append((sum(scores),-(id+1)))

greater = [i for i in ranks if i>ranks[0]]
print(len(greater)+1)