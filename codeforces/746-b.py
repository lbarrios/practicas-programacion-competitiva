#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/746/B

n = input()
word = list(input())

if len(word)<=2:
	print(''.join(word))
	exit()

decoded = list()

dlen = 0
izq = len(word)%2==0
for c in word:
	if izq:
		decoded = [c] + decoded
	else:
		decoded.append(c)
	izq = not izq

print(''.join(decoded))
