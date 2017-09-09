from sys import stdin
import math

def is_jolly(t):
    cantidad = t[0]
    diferencias = list()
    for i in range(1,cantidad):
        diferencias.append(int(math.fabs(t[i] - t[i+1])))
    diferencias.sort()
    for i in range(cantidad-1):
        if not diferencias[i] == i+1:
            return False
    return True


for line in stdin:
    T = list(map(int,line.split()))
    print("Jolly" if is_jolly(T) else "Not jolly")