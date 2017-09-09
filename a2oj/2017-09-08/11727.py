T = int(input())
for testcase in range(T):
    valores = list(map(int, input().split()))
    valores.sort()
    print("Case %s: %s" % (testcase + 1, valores[1]))
