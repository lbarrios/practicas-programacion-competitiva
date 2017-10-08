# [1112 - Mice and Maze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3553)

## Description

A set of laboratory mice is being trained to escape a maze. The maze is made up of cells, and each
cell is connected to some other cells. However, there are obstacles in the passage between cells and
therefore there is a time penalty to overcome the passage Also, some passages allow mice to go one-way,
but not the other way round.

Suppose that all mice are now trained and, when placed in an arbitrary cell in the maze, take a
path that leads them to the exit cell in minimum time.

We are going to conduct the following experiment: a mouse is placed in each cell of the maze and
a count-down timer is started. When the timer stops we count the number of mice out of the maze.
Write a program that, given a description of the maze and the time limit, predicts the number of
mice that will exit the maze. Assume that there are no bottlenecks is the maze, i.e. that all cells have
room for an arbitrary number of mice.


### Input
The input begins with a single positive integer on a line by itself indicating the number of the cases
following, each of them as described below. This line is followed by a blank line, and there is also a
blank line between two consecutive inputs.

The maze cells are numbered 1, 2, . . . , N, where N is the total number of cells. You can assume
that N ≤ 100.

The first three input lines contain N, the number of cells in the maze, E, the number of the exit
cell, and the starting value T for the count-down timer (in some arbitrary time unit).

The fourth line contains the number M of connections in the maze, and is followed by M lines, each
specifying a connection with three integer numbers: two cell numbers a and b (in the range 1, . . . , N)
and the number of time units it takes to travel from a to b.

Notice that each connection is one-way, i.e., the mice can’t travel from b to a unless there is another
line specifying that passage. Notice also that the time required to travel in each direction might be
different.


### Output
For each test case, the output must follow the description below. The outputs of two consecutive cases
will be separated by a blank line.

The output consists of a single line with the number of mice that reached the exit cell E in at most
T time units.

### Sample Input
```
1

4
2
1
8
1 2 1
1 3 1
2 1 1
2 4 1
3 1 1
3 4 1
4 2 1
4 3 1
```

### Sample Output
```
3
```

## Solving

### Problem Model
We need to calculate the numbers of mice that reach the cell E in at most T time units.

We can represent this problem as a directed weighted graph, being every cell a vertex, 
and every connection between the cells A and B an edge between the respective nodes A and B.

Given a connection between A and B nodes in the graph, 
the time units it takes to travel from the cell A to the cell B 
will be the weight of the corresponding edge. 
The length of a path between two nodes will be the sum of the weight of its edges.
 
Given that we are interested in the paths of length <= T (the maximum time units) 
that ends in the cell E, we can start from exit cell E, 
and walk only through the paths that ends in E,
searching for every mice that is at least at distance T.
Note that we will be doing this in the opposite direction of the paths.
This is, we can go from A to B if there is a connection from B to A.

Having this in mind, the most easy way for doing this is to simply reverse the direction of all the edges of the graph.
This is, if the input says there is an edge from nodes A to B, we store an edge from nodes B to A.

### Avoiding loops, finding the minimum path
Given a graph with loops, we don't want to iterate inside the loops,
because we know the mice will take the minimum path, and if there is a path with loops, 
it is surely _not minimum_. Even more, given the end vertex E and some other A, 
if there are K different paths from A to E, we are only interested in the one 
that satisfies being the minimum.

Given that we are working with non-negative weights, we can use Dijkstra algorithm, from node E,
stopping it for any path being greater than the maximum time units (being the small size of
the input, maybe this last condition is not necessary).