#!/usr/bin/env python3
# http://codeforces.com/problemset/problem/218/A

n, k = map(int,input().split())
y_points = list(map(int,input().split()))

k_tot=0
last_odd = len(y_points)-2 if (len(y_points)-1)%2==0 else len(y_points)-1
for i in range(last_odd,0,-2):
	if k_tot<k:
		if (y_points[i]-1)>y_points[i+1] and (y_points[i]-1)>y_points[i-1]:
			k_tot += 1
			y_points[i]-=1

print(" ".join(map(str,y_points)))
