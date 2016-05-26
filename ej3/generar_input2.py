#!/usr/bin/env python3
import random

max_testcases = 18
max_size = 75
min_int = -100
max_int = 1000

print(max_testcases)
for t in range(max_testcases):
	print(max_size)
	for row in range(max_size):
		print(" ".join([str(random.randint(-100,100)) for i in range(75)]))
