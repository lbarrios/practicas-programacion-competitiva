#!/usr/bin/env python3

n = int(input())
numbers = input().split()

fives=0
zeroes=0
for n in numbers:
	if n=='5':
		fives+=1
	else:
		zeroes+=1

if zeroes==0:
	print("-1")
	exit()

if(fives<9):
	print('0')
else:
	print('555555555'*int(fives/9)+'0'*zeroes)