for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ms = 1001 # min split
    for i in range(1, n):
        ms = min(a[i]-a[i-1], ms)
    print(ms)