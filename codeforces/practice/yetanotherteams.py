for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    t = 1
    a.sort()
    for i in range(1, n):
        if abs(a[1]-a[i-1] <= 1):
            t = 2
            break
    print(t)