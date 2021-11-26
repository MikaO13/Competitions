for _ in range(int(input())):
    a, b, n = map(int, input().split())
    c = 0
    while b <= n: 
        a, b = max(a, b), a+b
        c += 1
    print(c)