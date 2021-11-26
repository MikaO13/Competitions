import math
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(math.ceil(a / b)*b - a)