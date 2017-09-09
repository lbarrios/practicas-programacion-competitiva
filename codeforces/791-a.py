#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/791/A

l,b = map(int,input().split())
years = 0
while l<=b:
	years+=1
	b *= 2
	l *= 3

print(years)
