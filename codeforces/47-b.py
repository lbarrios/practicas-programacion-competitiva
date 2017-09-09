#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/47/B

w1 = input()
w2 = input()
w3 = input()

impossible=False
order = ''

c = {
	'A': 0,
	'B': 0,
	'C': 0,
}


if w1[1]=='<':
	c[w1[0]] -= 1
	c[w1[2]] += 1
else:
	c[w1[0]] += 1
	c[w1[2]] -= 1

if w2[1]=='<':
	c[w2[0]] -= 1
	c[w2[2]] += 1
else:
	c[w2[0]] += 1
	c[w2[2]] -= 1

if w3[1]=='<':
	c[w3[0]] -= 1
	c[w3[2]] += 1
else:
	c[w3[0]] += 1
	c[w3[2]] -= 1

r = [(c['A'],'A'),(c['B'],'B'),(c['C'],'C')]
r.sort()

if r[0][0]==r[1][0] or r[1][0]==r[2][0]:
	print('Impossible')
else:
	rs = r[0][1] + r[1][1] + r[2][1]
	print(rs)
