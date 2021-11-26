for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = 0
    for i in a: s+= i
    if s >= m: print(m)
    else: print(s)