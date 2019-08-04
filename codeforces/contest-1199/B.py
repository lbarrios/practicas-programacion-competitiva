#!/usr/bin/env python3
# http://codeforces.com/contest/1199/problem/B


H,L = list(map(int,input().split()))
print(((L*L)-(H*H))/(2*H))