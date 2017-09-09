from sys import stdin

for line in stdin:
    n, k = list(map(int, line.split()))
    resto = int(n % k)
    nuevos = int(n / k)
    total = n

    while nuevos > 0:
        total += nuevos
        resto += nuevos
        nuevos = 0
        if resto >= k:
            nuevos = int(resto / k)
            resto = resto % k
    print(total)
