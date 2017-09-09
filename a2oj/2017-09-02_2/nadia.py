#!/usr/bin/env python3

T = int(input())
for t in range(T):
	word = input().lower()
	nadia_word = list("nadia")
	for c in word:
		if len(nadia_word)==0:
			#print("\tbreak")
			break
		if c==nadia_word[0]:
			#print("\tc in nadia")
			nadia_word = nadia_word[1:]
	print("YES" if len(nadia_word)==0 else "NO")