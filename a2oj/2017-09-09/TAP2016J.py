#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.spoj.com/problems/TAP2016J/

def resolverTestcase(N,L,C):
    Ks = list(map(int,input().split()))
    Ks.sort()
    while len(Ks) > 0:
        k = Ks.pop()
        C -= k
        for i in range(1, L):
            if len(Ks) > 0:
                Ks.pop()
    print("S" if C>=0 else "N")

while True:
    try:
        N,L,C = map(int,input().split())
        resolverTestcase(N,L,C)
    except EOFError:
        break