def sumTuples(tuple1,tuple2):
    """Given two tuples, returns the pos-by-pos sum"""
    # return 
    return tuple(map(sum,zip(tuple1,tuple2)))

def move1A(pos):
    """Given a pos, it returns the Cartesian quadrant 1 movement A"""
    return sumTuples(pos,(1,2))
def move1B(pos):
    """Given a pos, it returns the Cartesian quadrant 1 movement B"""
    return sumTuples(pos,(2,1))

def move2A(pos):
    """Given a pos, it returns the Cartesian quadrant 2 movement A"""
    return sumTuples(pos,(-1,2))
def move2B(pos):
    """Given a pos, it returns the Cartesian quadrant 2 movement B"""
    return sumTuples(pos,(-2,1))

def move3A(pos):
    """Given a pos, it returns the Cartesian quadrant 3 movement A"""
    return sumTuples(pos,(-1,-2))
def move3B(pos):
    """Given a pos, it returns the Cartesian quadrant 3 movement B"""
    return sumTuples(pos,(-2,-1))

def move4A(pos):
    """Given a pos, it returns the Cartesian quadrant 4 movement A"""
    return sumTuples(pos,(1,-2))
def move4B(pos):
    """Given a pos, it returns the Cartesian quadrant 4 movement B"""
    return sumTuples(pos,(2,-1))

allMovements = (move1A,move1B,move2A,move2B,move3A,move3B,move4A,move4B)