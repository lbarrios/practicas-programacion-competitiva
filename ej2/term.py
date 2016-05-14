from sys import stderr

def clear():
    stderr.write("\x1b[2J\x1b[H")
    stderr.flush()