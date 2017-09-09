#!/usr/bin/env python3

T = int(input())
for t in range(T):
	N,K = map(int,input().split())
	candies = map(int,input().split())
	tot = 0
	for c in candies:
		tot += int(c/K)
	print(tot)