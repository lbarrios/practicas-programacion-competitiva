#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

DEBUG = False
DEBUG = True

def torus_max_sum(torus):
	""" given a torus, returns the max sum """
	max_sum = torus[0][0]
	for x in range(torus_size):
		for y in range(torus_size):
			S[x][y][0][0] = torus[x][y]
	for h in range(torus_size-1):
		for w in range(1, torus_size):
			for y in range(torus_size):
				for x in range(torus_size):
					S[x][y][w][h] = S[x][y][w-1][h] \
						+ torus[(x+w)%torus_size][(y+h)%torus_size]
					max_sum = max(max_sum, S[x][y][w][h])
	return max_sum

total_testcases = int(input()) # at most 18 testcases
for testcase in range(total_testcases):
	torus_size = int(input()) # 1<=torus_size<=75
	torus = list()
	for row in range(torus_size):
		#row_cells = [int(cell) for cell in input().split(' ')] # -100 <= row cell <= 100
		#torus.append(row_cells)
		row_cells = [int(cell) for cell in input().split(' ')] # -100 <= row cell <= 100
		torus.append(row_cells)
	#torus = np.array(torus)
	#S = dict() # empty the subproblem dict
	#S = np.empty([torus_size, torus_size, torus_size, torus_size])
	S = [[[[ 0 for a in range(torus_size)]
		for b in range(torus_size)]
			for c in range(torus_size)]
				for d in range(torus_size)]
	output = torus_max_sum(torus)
	print(output)