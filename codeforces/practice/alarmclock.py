import math
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b >= a: print(b)
    elif c <= d: print(-1)
    else: 
        print(b + math.ceil((a-b)/(c-d))*c)