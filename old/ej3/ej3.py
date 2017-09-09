#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DEBUG = False
#DEBUG = True

def torus_max_sum_for_size(torus, size):
	if DEBUG: print("\tSearching for size: %s"%size)
	sums = list()
	torus_size = len(torus)
	for cell_pos in range(0,torus_size**2):
		sum = 0
		start_row = cell_pos // torus_size
		start_column = cell_pos % torus_size
		if DEBUG: print("\t\tSearching a subsquare of size %s begining at cell pos %s = (%s,%s)"%(size,cell_pos,start_row,start_column))
		for r in range(size):
			row = ( start_row + r ) % torus_size
			for c in range(size):
				column = (start_column + c) % torus_size
				if DEBUG: print("\t\t\t(%s,%s) = %s"%(row,column,torus[row][column]))
				sum += torus[row][column]
		sums.append(sum)
	if DEBUG: print("\tsums = %s"%sums)
	if DEBUG: print("\tmax sum = %s"%max(sums))
	return max(sums)

def torus_max_sum(torus):
	""" given a torus, returns the max sum """
	max_sub_rectangle_size = len(torus)
	#wrapped_torus = [ row+row for row in torus ] * 2
	max_sum = torus[0][0]
	for size in range(1,max_sub_rectangle_size+1):
		max_sum_for_size = torus_max_sum_for_size(torus,size)
		max_sum = max(max_sum, max_sum_for_size)
	return max_sum

testcases = int(input())
# at most 18 testcases
for testcase in range(testcases):
	if DEBUG: print("Testcase %s:"%(testcase+1,))
	torus_size = int(input())
	# 1<=torus_size<=75
	torus = list()
	for row in range(torus_size):
		row_cells = [int(cell) for cell in input().split(' ')]
		# -100 <= row cell <= 100
		torus.append(row_cells)
	if DEBUG: print("\tTorus: %s"%(torus,))
	output = torus_max_sum(torus)
	print(output)
