import math
n, k = map(int, input().split())

if k >= n: print(2)
else: print(math.ceil(n * 2 / k))