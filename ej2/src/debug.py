from term import clear
from grapher import printBoard
from time import sleep
DEBUG_SPEED=0.00005
WIN_PAUSE=5

def DEBUG_MOVEMENT(N,movements):
    clear()
    DEBUG_BOARD = [['' for i in xrange(N)] for i in xrange(N)]
    i = 0
    for mov in movements:
        i += 1
        DEBUG_BOARD[mov[1]-1][mov[0]-1] = i
    printBoard(DEBUG_BOARD,i)
    sleep(DEBUG_SPEED)

def DEBUG_BAD_MOVEMENT(N,movements):
    clear()
    DEBUG_BOARD = [['' for i in xrange(N)] for i in xrange(N)]
    i = 0
    for mov in movements:
        i += 1
        DEBUG_BOARD[mov[1]-1][mov[0]-1] = i
    printBoard(DEBUG_BOARD,len(movements),"BAD")
    sleep(DEBUG_SPEED)


def DEBUG_WIN(N,movements):
    clear()
    DEBUG_BOARD = [['' for i in xrange(N)] for i in xrange(N)]
    i = 0
    for mov in movements:
        i += 1
        DEBUG_BOARD[mov[1]-1][mov[0]-1] = i
    printBoard(DEBUG_BOARD,len(movements),"WIN")
    sleep(WIN_PAUSE)
