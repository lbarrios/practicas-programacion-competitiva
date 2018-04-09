#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Practice Round - Problem A

testcases = int(input())

for t in range(testcases):
    N = int(input())
    N_cities = list(map(int, input().split()))
    P = int(input())
    if t+1<testcases:
        input() # there is an empty line between testcases