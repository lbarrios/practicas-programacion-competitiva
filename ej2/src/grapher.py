import math
RESET    ='\033[0m'
BOLD     ='\033[01m'
FGCYAN   ='\033[36m'
FGPURPLE ='\033[35m'
BGGREY   ='\033[47m'
FGBLACK  ='\033[30m'
BGRED    ='\033[41m'

def printRow(row,i,maxMoveWidth, status):
    if status=="BAD":
        LASTMOVECOLOR=BOLD+FGBLACK+BGRED
    else:
        LASTMOVECOLOR=BOLD+FGPURPLE#FGPURPLE+BGGREY
    r = "|"
    for c in row:
        if c!=i:
            r+=RESET+"{0:^{1}}".format(str(c),maxMoveWidth)+"|"
        else:
            r+=LASTMOVECOLOR+"{0:^{1}}".format(str(c) if status!="BAD" else "X",maxMoveWidth)+RESET+"|"
    print r

def printRowWin(row,i,maxMoveWidth):
    r = "|"
    for c in row:
        r+="{0:^{1}}".format(str(c),maxMoveWidth)+"|"
    print r

def printBoard(board,i, status=False):
    N = len(board)
    boardSize = N*N
    maxMoveWidth = int(math.ceil(math.log10(boardSize)))
    if maxMoveWidth%2==0:
        maxMoveWidth+=1
    if maxMoveWidth<4:
        maxMoveWidth+=2
    for row in board:
        if status!="WIN":
            print "-"*(N*maxMoveWidth+N+1)
            printRow(row,i,maxMoveWidth,status)
        else:
            print FGCYAN+"-"*(N*maxMoveWidth+N+1)
            printRowWin(row,i,maxMoveWidth)

    print "-"*(N*maxMoveWidth+N+1)