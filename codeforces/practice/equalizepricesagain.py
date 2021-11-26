import math
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = 0
    for i in a: s += i
    print(math.ceil(s / n))