#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam Kickstart 2018 - Round A - Problem A

testcases = int(input())


def check_all_even(N):
    for d in range(len(N)):
        if int(N[d]) % 2 == 1:
            return False
    return True


for t in range(testcases):
    N = input()
    if check_all_even(N):
        print("Case #%s: 0" % (t + 1,))
        continue

    if len(N) == 1:
        print("Case #%s: %s" % (t + 1, int(N) % 2))
        continue

    # there is at least one odd digit
    for digit in range(len(N)):
        if int(N[digit]) % 2 == 0:
            continue
        adds = 10 ** (len(N) - 1 - digit)
        if len(N) - 1 != digit:
            adds -= int(N[digit + 1:])
        if (digit == 0 and N[0] == '9') or (digit > 0 and N[digit] == '9' and int(N[digit - 1]) % 2 == 0):
            adds += (10 ** (len(N) - digit))
        break

    subs = adds
    for digit in range(len(N)):
        if int(N[digit]) % 2 == 0:
            continue
        N_sub = "8" * (len(N) - (digit + 1))
        if int(N[digit]) - 1 != 0:
            N_sub = str(int(N[digit]) - 1) + N_sub
        if N_sub != "":
            subs = int(N[digit:]) - int(N_sub)
        break

    print("Case #%s: %s" % (t + 1, min(adds, subs)))
