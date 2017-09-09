#!/usr/bin/env python3

n = int(input())
total = 0
for problem in range(n):
	a,b,c = map(int,input().split())
	if a+b+c > 1: total+=1

print(total)