MAX_N = 65536
es_primo = [True] * (MAX_N + 1)
primos = list()

def marcar_multiplos(step, max_n):
    global es_primo
    for i in range(step, max_n, step):
        es_primo[i] = False

def criba(max_n):
    global es_primo, primos
    primos.append(1)
    for i in range(2, max_n + 1):
        if es_primo[i]:
            primos.append(i)
            marcar_multiplos(i, max_n + 1)
    return primos

primos = criba(MAX_N)

T = int(input())
while T != 0:
    root = T ** .5
    apagada = False
    for i in primos:
        if i > root:
            break
        if T % i == 0:
            apagada = not apagada
    if apagada:
        print("no")
    else:
        print("yes")
    T = int(input())
