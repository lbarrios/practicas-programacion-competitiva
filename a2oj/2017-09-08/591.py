import math
n = int(input())
set = 0
while n != 0:
    set += 1
    heights = list(map(int, input().split()))
    avg = sum(heights) / len(heights)
    total = 0
    for x in heights:
        total += math.fabs(avg-x)
    print("Set #%s"%set)
    print("The minimum number of moves is %s."%int(total/2))
    print("")
    n = int(input())