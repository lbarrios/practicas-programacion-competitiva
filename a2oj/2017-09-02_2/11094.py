#!/usr/bin/env python3

while True:
	try:
		M,N = map(int,input().split())
		mapa=list()
		for i in range(M):
			mapa.append(input())
		X,Y = map(int,input().split())
		resolver_mapa(mapa)
		input()
	except EOFError:
		break