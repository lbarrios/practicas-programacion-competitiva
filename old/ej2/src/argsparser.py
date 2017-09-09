import argparse
parser = argparse.ArgumentParser(description='''Given a size N and i,j positions
this program outputs the movements corresponding to a closed "Knight Tour" from
a (i,j) starting position on a NxN board.''')
parser.add_argument('N', type=int, help='The size of the board')
parser.add_argument('i', type=int, help='The horizontal position of the horse')
parser.add_argument('j', type=int, help='The vertical position of the horse')
parser.add_argument('--debug', action="store_true", help="debug mode")
params = parser.parse_args()
N = params.N
startingPosition=(params.i,params.j)
DEBUG=params.debug