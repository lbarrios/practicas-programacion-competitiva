#!/usr/bin/env python3
# http://codeforces.com/contest/1199/problem/A

n,x,y = list(map(int,input().split()))
A = list(map(int,input().split()))

for i in range(n):
    if A[i] == min(A[max(0,i-x):min(n,i+y+1)]):
        print(i+1)
        exit()

for i in range(x):
    if A[i] == min(A[:y+i]):
        print(i+1)
        exit()

for i in range(y):
    last = n-1
    if A[last-i] == min(A[last-i-x:]):
        print(last-i+1)
        exit()

desc = 0
asc = 0
for ix in range(x, n-y):
    ix += 1

print(ix)