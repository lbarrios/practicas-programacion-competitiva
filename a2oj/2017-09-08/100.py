from sys import stdin

cycles = {
    1: 1
}

def cycle(k):
    if not k in cycles:
        if k%2==1:
            cycles[k] = cycle(int((3*k)+1)) + 1
        else:
            cycles[k] = cycle(int(k/2)) + 1
    return cycles[k]


for line in stdin:
    i, j = map(int, line.split())
    imin = min(i,j)
    jmax = max(i,j)
    maximum_cycle = 0
    for k in range(imin, jmax + 1):
        maximum_cycle = max(maximum_cycle, cycle(k))
    print(i,j,maximum_cycle)
