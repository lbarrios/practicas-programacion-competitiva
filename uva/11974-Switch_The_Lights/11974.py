#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3125

def solve_for_switches(lamps_for_switch):
    # initially all the states are unreachable
    # except the initial state (all on) that is reachable with 0 switches
    states_list = list()
    states_count = [switch_count + 1 for i in range((2 ** lamp_count))]
    defined_state = [False for i in range((2 ** lamp_count))]
    states_count[initial_state] = 0
    defined_state[initial_state] = True
    states_list.append(initial_state)

    new_states = states_list
    for step in range(1, switch_count + 1):
        # in this part, states will store the minimum number of switches needed to reach
        # to the state represented by the "ith" key of the dict, using it as a binary mask
        # eg., the state 5 will be 0101 = switch 0 on, switch 1 off, switch 2 on, switch 3 off

        # now try all the switches combinations
        last_states = new_states
        new_states = list()
        for switch in lamps_for_switch:
            for s in last_states:
                current_state = s ^ switch
                # store the number of switches used to reach to this state, if it's less than the previous stored
                if not defined_state[current_state]:
                    defined_state[current_state] = True
                    new_states.append(current_state)
        for state in new_states:  # define all the new discovered states
            states_count[state] = step
            states_list.append(state)

        if defined_state[0]:
            break

    ret_states_list = list()
    for state in states_list:
        ret_states_list.append((states_count[state], state))
    ret_states_list.sort()

    return ret_states_list, defined_state, states_count


testcase_count = int(input())
for testcase in range(testcase_count):
    lamp_count, switch_count = map(int, input().split())
    lamps_for_switch = list()
    for switch in range(switch_count):
        # store as the int that results from translating the switch from binary to int
        # eg., the switch "0 1 0 1" is stored as 5
        lamps_for_switch.append(int(input().replace(" ", ""), 2))

    initial_state = (2 ** lamp_count) - 1
    switches_A = lamps_for_switch[:int(len(lamps_for_switch) / 2)]
    states_list_A, defined_state_A, states_count_A = solve_for_switches(switches_A)
    switches_B = lamps_for_switch[int(len(lamps_for_switch) / 2):]
    states_list_B, defined_state_B, states_count_B = solve_for_switches(switches_B)

    win = False
    win_count = 9999999

    for (a_count, a) in states_list_A:
        b = initial_state ^ a
        if defined_state_B[b]:
            win = True
            win_count = min(win_count, a_count + states_count_B[b])
    if defined_state_A[0]:
        win = True
        win_count = min(win_count, states_count_A[0])
    if defined_state_B[0]:
        win = True
        win_count = min(win_count, states_count_B[0])

    if win:
        print("Case %s: %s" % (testcase + 1, win_count))
    else:
        print("Case %s: IMPOSSIBLE" % (testcase + 1))
