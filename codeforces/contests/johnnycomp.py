for _ in range(int(input())):
    a, b = map(int, input().split())
    t = 0
    a = bin(a)[2:]
    b = bin(a)[2:]

    i1 = len(a)-1
    i2 = len(b)-1

    while a[i1] == '0':
        i1 -= 1
    while b[i2] == '0':
        i2 -= 1
    
    a2 = a[:i1+1]
    b2 = b[:i2+1]

    if a2 != b2:
        print(-1)
    else:
        x = abs(len(a)-len(b))
        ans = x//3
        x %= 3
        ans += x//2
        x %= 2
        ans += x
        print(ans)