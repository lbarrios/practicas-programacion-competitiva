#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.spoj.com/problems/TAP2016L/

def goNext(nodes, fN, sN, N, lastMove):
	try: nN = next(nodes)
	except StopIteration: return True
	if nN>N or nN==fN or sN<=2: return False
	if lastMove[1]!='D':
		if nN==sN+2: return goNext(nodes, sN, nN, N, "LU")
		if nN==sN+1: return goNext(nodes, sN, nN, N, "RU")
	if sN==nN+2: return goNext(nodes, sN, nN, N, "LD")
	if sN==nN+1: return goNext(nodes, sN, nN, N, "RD")
	return False

def testcase(N,K):
	nodes = iter(list(map(int,input().split())))
	fN, sN = next(nodes), next(nodes) # N>=2
	canResolve = False
	if sN==fN+2: canResolve = goNext(nodes, fN, sN, N, "LU")
	if sN==fN+1 and fN!=1: canResolve = goNext(nodes, fN, sN, N, "RU")
	if fN==sN+2: canResolve = goNext(nodes, fN, sN, N, "LD")
	if fN==sN+1 and fN!=2: canResolve = goNext(nodes, fN, sN, N, "RD")
	print("S" if canResolve else "N")
while True:
	try:
		N,K = map(int,input().split())
		testcase(N,K)
	except:
		break
