import math
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    print(a*math.ceil(k/2) - b*(k//2))