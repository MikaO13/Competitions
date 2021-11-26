for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    b = b // 2
    t = 0
    if h >= c:
        t += min(b, p)*h
        b -= min(b, p)
        t += min(b, f)*c
    else:
        t += min(b, f)*c
        b -= min(b, f)
        t += min(b, p)*h
    print(t)