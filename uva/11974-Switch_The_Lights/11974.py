#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3125

testcase_count = int(input())
for testcase in range(testcase_count):
    lamp_count, switch_count = map(int, input().split())
    lamps_for_switch = list()
    for switch in range(switch_count):
        # store as the int that results from translating the switch from binary to int
        # eg., the switch "0 1 0 1" is stored as 5
        lamps_for_switch.append(int(input().replace(" ", ""), 2))


    def make_states(lamps_for_switch):
        # in this function, states will store the minimum number of switches needed to reach
        # to the state represented by the "ith" position of the list, using it as a binary mask
        # eg., the state 5 will be 0101 = switch 0 on, switch 1 off, switch 2 on, switch 3 off

        # initially all the states are unreachable
        # except the initial state (all on) that is reachable with 0 switches
        states = [(switch_count + 1) for state in range(2 ** lamp_count)]
        states[initial_state] = (0)

        # now try all the switches combinations
        for i in range(2 ** len(lamps_for_switch)):
            # we are using the integer "i" as a bit mask
            switches_used = bin(i)[2:]
            current_state = initial_state
            # start by 11...11, and apply the corresponding switches
            for s in range(len(switches_used)):
                if switches_used[s] == '1':
                    current_state ^= lamps_for_switch[s]
            # store the number of switches used to reach to this state, if it's less than the previous
            states[current_state] = min(states[current_state], switches_used.count("1"))
        return states


    initial_state = (2 ** lamp_count) - 1
    states_A = make_states(lamps_for_switch[:int(switch_count / 2)])
    states_B = make_states(lamps_for_switch[int(switch_count / 2):])

    min_switches_needed = switch_count + 1  # start with an impossible solution
    for state in range(len(states_A)):
        not_state = state ^ initial_state
        min_switches_needed = min(min_switches_needed, states_A[state] + states_B[not_state])
    for state in range(len(states_B)):
        not_state = state ^ initial_state
        min_switches_needed = min(min_switches_needed, states_B[state] + states_A[not_state])

    print("Case %s: %s" % (testcase + 1, min_switches_needed if min_switches_needed <= switch_count else "IMPOSSIBLE"))
