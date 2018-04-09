#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Codejam 2018 - Saving The World Again

MAX_P_LEN = 30

testcases = int(input())


def total_damage(damage_base2):
    total = 0
    for i in range(len(damage_base2)):
        total += 2 ** i * damage_base2[i]
    return total


for t in range(testcases):
    d, instructions = input().split()
    d = int(d)

    # check if this is an impossible problem
    if instructions.count("S") > d:
        print("Case #%s: IMPOSSIBLE" % (t + 1))
        continue

    # generate a better representation of the input
    damage_base2 = [0] * (instructions.count("C") + 1)
    damage_index = 0
    for inst in instructions:
        if inst == "C":
            damage_index += 1
        else:
            damage_base2[damage_index] += 1

    # clear the last indexes while they're 0
    i = len(damage_base2) - 1
    while i>0 and damage_base2[i] == 0:
        del damage_base2[-1]
        i -= 1

    # at this point i'm sure i'm going to solve the problem
    min_swaps = 0
    while d < total_damage(damage_base2):
        min_swaps += 1
        damage_base2[-1] -= 1
        # the len of the list is always > 1, because if not the problem is impossible
        damage_base2[-2] += 1
        if damage_base2[-1] == 0:
            del damage_base2[-1]

    print("Case #%s: %s" % (t + 1, min_swaps))
