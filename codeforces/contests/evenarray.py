import math
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    e = 0
    o = 0
    be = 0
    bo = 0

    for i in range(n):
        if a[i] % 2 == 0: 
            e += 1
            if i % 2 == 1:
                be += 1
        else:
            o += 1
            if i % 2 == 0:
                bo += 1
    if math.ceil(n / 2) == e and n // 2 == o:
        print((be + bo)//2)
    else:
        print(-1)