#!/usr/bin/env python3

LS = list()
US = list()

while True:
	try:
		L,U = input().split()
		L=int(L)
		U=int(U)
		LS.append(L)
		US.append(U)		
	except EOFError:
		break

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes


primes = primes_sieve(max(US))

print("Primos calculados hasta %s"%(max(US),))

for li in range(len(LS)):
	l=LS[li]
	u=US[li]
	min_d = u
	min_pos = -1
	max_d = -1
	max_pos = -1
	have_diffs = False
	for i in range(len(primes)-1):
		if primes[i]>=l and primes[i+1]<=u:
			d = primes[i+1]-primes[i]
			#print("%s %s %s"%(d, primes[i+1],primes[i]))
			if d<min_d:
				#print("found %s, %s"%(d,primes[i]))
				min_d = d
				min_pos = i
			if d>max_d:
				max_d = d
				max_pos = i
			have_diffs = True
		if primes[i+1]>u:
			#print("breaking on %s"%primes[i])
			break
	if have_diffs:
		min_a = primes[min_pos]
		min_b = primes[min_pos+1]
		max_a = primes[max_pos]
		max_b = primes[max_pos+1]
		print("%s,%s are closest, %s,%s are most distant."%(min_a, min_b, max_a, max_b))
	else:
		print("There are no adjacent primes.")