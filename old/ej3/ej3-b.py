#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DEBUG = False
#DEBUG = True

TSFPAS = dict()
def torus_sum_for_position_and_size(torus_testcase, starting_position, size):
	"""
	assume that I previously calculated
	torus_max_sum_for_size(torus,size-1),
	that gives for every position the value of
	torus_sum_for_position_and_size(torus, position, size-1)
	then I just add the borders
	"""
	torus = testcases[torus_testcase]
	torus_size = len(torus)
	starting_row = starting_position // torus_size
	starting_col = starting_position % torus_size
	if DEBUG: print("\t\tcalculating torus sum for position %s=(%s,%s) and size %s"%(starting_position,starting_row,starting_col,size))
	key = "%s,%s"%(starting_position,size)
	if DEBUG: print("\t\t\tmemoization key is '%s'"%key)
	if size == 2:
		if DEBUG: print("\t\t\tsize=2, there is no previous result")
		cell_1 = torus[starting_row][starting_col]
		cell_2 = torus[(starting_row+1)%torus_size][starting_col]
		cell_3 = torus[starting_row][(starting_col+1)%torus_size]
		cell_4 = torus[(starting_row+1)%torus_size][(starting_col+1)%torus_size]
		TSFPAS[key] = cell_1+cell_2+cell_3+cell_4
		if DEBUG: print("\t\t\tmemoizing TSFPAS['%s']=%s"%(key,TSFPAS[key]))
	else:
		previous_key = "%s,%s"%(starting_position,size-1)
		inner_sum = TSFPAS[previous_key]
		if DEBUG: print("\t\t\tusing memoizated value TSFPAS['%s']=%s"%(previous_key,inner_sum))
		right_col = (starting_col+size-1)%torus_size
		bottom_row = (starting_row+size-1)%torus_size
		if DEBUG: print("\t\t\tright col: %s, bottom_row: %s"%(right_col,bottom_row))
		outer_right = [torus[row%torus_size][right_col] for row in range(starting_row,starting_row+size)]
		if DEBUG: print("\t\t\touter right: %s"%outer_right)
		outer_bottom = [torus[bottom_row][col%torus_size] for col in range(starting_col,starting_col+size)]
		if DEBUG: print("\t\t\touter bottom: %s"%outer_bottom)
		outer_last = torus[bottom_row][right_col] # im adding this two times
		if DEBUG: print("\t\t\touter last: %s"%outer_last)
		TSFPAS[key] = (inner_sum + sum(outer_right) + sum(outer_bottom) - outer_last)
		if DEBUG: print("\t\t\tmemoizing TSFPAS['%s']=%s"%(key,TSFPAS[key]))
	return TSFPAS[key]

def torus_max_sum_for_size(torus_testcase, size):
	if DEBUG: print("\tSearching for size: %s"%size)
	torus = testcases[torus_testcase]
	max_sum = torus[0][0]
	if size == 1:
		torus_c = [j for i in torus for j in i]
		if DEBUG: print("\t\tsize=1, returning max(torus)=%s"%max(torus_c))
		return max(torus_c)
	else:
		torus_size = len(torus)
		for cell_pos in range(0,torus_size**2):
			max_sum = max(max_sum, torus_sum_for_position_and_size(torus_testcase, cell_pos, size))
		return max_sum

def torus_max_sum(torus_testcase):
	""" given a torus, returns the max sum """
	torus = testcases[torus_testcase]
	max_sub_rectangle_size = len(torus)
	#wrapped_torus = [ row+row for row in torus ] * 2
	max_sum = torus[0][0]
	for size in range(1,max_sub_rectangle_size+1):
		max_sum_for_size = torus_max_sum_for_size(torus_testcase,size)
		max_sum = max(max_sum, max_sum_for_size)
	return max_sum

total_testcases = int(input())
testcases = dict()
# at most 18 testcases
for testcase in range(total_testcases):
	if DEBUG: print("Testcase %s:"%(testcase+1,))
	torus_size = int(input())
	# 1<=torus_size<=75
	testcases[testcase] = list()
	for row in range(torus_size):
		row_cells = [int(cell) for cell in input().split(' ')]
		# -100 <= row cell <= 100
		testcases[testcase].append(row_cells)
	if DEBUG: print("\tTorus: %s"%(testcases[testcase],))
	TSFPAS = dict() # empty the memoization dict to save memory
	output = torus_max_sum(testcase)
	print(output)
