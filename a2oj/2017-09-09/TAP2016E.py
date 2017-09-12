#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.spoj.com/problems/TAP2016E/


def resolverTestcase(N,M):
    buttonToApp = [[]]*N
    for n in range(N):
        buttonToApp[n] = list(map(int,input().split()))
    print(buttonToApp)

while True:
    try:
        N,M = map(int,input().split())
        resolverTestcase(N,M)
    except EOFError:
        break