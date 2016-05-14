#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from time import sleep
from movements import allMovements
from grapher import printBoard
from argsparser import N, startingPosition, DEBUG
from term import clear
from debug import *

boardSize = N*N
endingPositions=[move(startingPosition) for move in allMovements]

def isOutsideOfTheBoard(pos):
    return pos[0]<1 or pos[1]<1 or pos[0]>N or pos[1]>N

def movementIsRepeated(pos, movements):
    return pos in movements

def isLastMovement(movements):
    return len(movements)==boardSize

def isOneMovementFromTheStart(pos):
    return pos in endingPositions

def backtrack(pos, movements):
    """Given a pos and a movement list, calculates the closed KT solution,
    or returns false if there is no posible KT"""
    movements.append(pos)
    if DEBUG: DEBUG_MOVEMENT(N,movements)

    if isLastMovement(movements):
        return pos if isOneMovementFromTheStart(pos) else False

    for move in allMovements:
        if isOutsideOfTheBoard(move(pos)):
            continue
        if movementIsRepeated(move(pos), movements):
            continue
        bt = backtrack(move(pos), movements)
        if bt:
            if DEBUG: DEBUG_WIN(N,movements)
            return movements
        else:
            del movements[-1]

movements = backtrack(startingPosition, [])
if not movements:
    clear()
    print "No se encontró una solución"
    exit()

# print step-to-step board
board = [['' for i in xrange(N)] for i in xrange(N)]

i = 1
for mov in movements:
    board[mov[0]-1][mov[1]-1] = i
    printBoard(board,i,"BAD")
    i += 1
    sleep(0.5)
    clear()
