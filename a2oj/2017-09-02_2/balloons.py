#!/usr/bin/env python3

T = int(input())
for t in range(T):
	N, c_easy, c_hard = map(int, input().split())
	colors = list(map(int, input().split()))
	easy_ok = True
	hard_ok = True
	if colors[0]==c_easy:
		easy_ok = False
	if colors[-1]==c_hard:
		hard_ok = False
	
	if easy_ok and hard_ok:
		print("OKAY")
	if easy_ok and not hard_ok:
		print("HARD")
	if not easy_ok and hard_ok:
		print("EASY")
	if not easy_ok and not hard_ok:
		print("BOTH")