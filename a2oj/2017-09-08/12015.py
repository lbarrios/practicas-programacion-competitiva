T = int(input())
for t in range(T):
    print("Case #%s:" % (t + 1,))
    pages = list()
    maxv = -1
    for i in range(10):
        p, v = input().split()
        maxv = max(maxv, int(v))
        pages.append((int(v), p))
    pages_max = [page for page in pages if page[0] == maxv]
    for page in pages_max:
        print(page[1])
