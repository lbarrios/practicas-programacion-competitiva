#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/734/A

n = int(input())


s = input()
a=0
d=0
for c in s:
	if c=='A':
		a+=1
	else:
		d+=1

if a==d:
	print("Friendship")
if a>d:
	print("Anton")
if a<d:
	print("Danik")
