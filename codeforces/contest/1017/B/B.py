#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pairs = [0,0,0,0]

n = int(input())
a = input()
b = input()

for i in range(n):
    if a[i]=="0" and b[i]=="0":
        pairs[0b00] += 1
    elif a[i]=="0" and b[i]=="1":
        pairs[0b01] += 1
    elif a[i]=="1" and b[i]=="0":
        pairs[0b10] += 1
    elif a[i]=="1" and b[i]=="1":
        pairs[0b11] += 1

total = total_00 = pairs[0b00]*pairs[0b10] + pairs[0b00]*pairs[0b11] + pairs[0b10]*pairs[0b01]
print(total)