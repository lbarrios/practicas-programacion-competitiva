#!/usr/bin/env python3

T = int(input())

def is_english(word):
	return not '#' in word

for i in range(T):
	words_count = int(input())
	words = input().split()
	have_english = False
	english_pos = -1
	for i in range(len(words)):
		if is_english(words[i]):
			have_english = True
			english_pos = i
	if not have_english:
		print (" ".join(words))
	else:
		res = list()
		for i in range(english_pos+1,len(words)):
			res.append(words[i])
		res.append(words[english_pos])
		for i in range(english_pos):
			res.append(words[i])
		print (" ".join(res))
