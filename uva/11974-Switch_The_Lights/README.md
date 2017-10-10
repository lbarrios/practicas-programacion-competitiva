# [11974 - Switch The Lights](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3125)

## Description
Kaunas University of Technology has bought a new light toggling system from one of the cheapest
manufacturers in China. It consists of N lamps and M switches. Each switch has a subset of lights
assigned to it, and when toggled, it changes the state of all the lights in the subset from on to off and
vice versa. Also the system contains the main switch which is used to turn turn off all lights.

The authorities installed the switches at different locations in the univerisity. But one day the main
switch went down. Now they are not able to turn off all lights by using the main switch. Unfortunately
noone understands the Chineese documentation of the system, so we must wait for support from
manufacturers. But we have good programmers, and we are interested in finding the minimal number
of switches required to turn off all lights in the university. Initially, all lights are turned on.

## Input
The first line of input contains the number of tests T (T ≤ 50). Each test case is a set of lines. First
line of each test case contains 2 positive integers N (N ≤ 15) and M (M ≤ 100) separated by a space
character. Next M lines contain N integers K (Ki ∈ {1, 0}) separated by a space character (if the i-th
integer is 1 then the i-th light is toggled by the switch).

## Output
For each test case output a single line ‘Case T: N’. Where T is the test case number (starting from
1) and N is the minimal number of switches required. If it is impossible to turn off all lights N should
be equal to ‘IMPOSSIBLE’.

## Sample Input
```
2
2 2
0 1
1 0
3 2
1 0 1
1 1 0
```

## Sample Output
```
Case 1: 2
Case 2: IMPOSSIBLE
```
