for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if b < 2*a:
        if n % 2 == 0: print(b*n//2)
        else: print(b*(n//2)+a)
    else:
        print(a*n)