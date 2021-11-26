import math
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if m==0: print(0)
    else:
        if n//k >= m:
            ma = m
            print(ma*2-m)
        else:
            ma = n//k
            print(ma-math.ceil((m-ma)/(k-1)))