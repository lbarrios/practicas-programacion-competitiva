#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3125

testcase_count = int(input())
lamp_count,switch_count = map(int, input().split())

lamps_for_switch = list()
for switch in range(switch_count):
	lamps_for_switch.append(list(map(bool,map(int,input().split()))))

print(lamps_for_switch)

initial_state = [True for lamp in range(lamp_count)]
print(initial_state)

