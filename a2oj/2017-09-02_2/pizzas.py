#!/usr/bin/env python3

T = int(input())
for t in range(T):
	N = int(input())
	costs = map(int,input().split())
	print("Case %s: %s"%(t+1, sum(costs)))