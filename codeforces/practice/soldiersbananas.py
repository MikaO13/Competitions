import math
k, n, w = map(int, input().split())
t = k * sum(range(1, w+1)) - n 
if t <= 0:
    print(0)
else:
    print(t)