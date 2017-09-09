#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/677/A

n, h = map(int,input().split())

tot = 0
friends = map(int,input().split())
for f in friends:
	tot = tot+2 if f>h else tot+1

print(tot)
