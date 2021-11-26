for _ in range(int(input())):
    n = int(input())
    t = 0
    if n % 5 == 0:
        while n % 5 == 0:
            n //= 5
            t += 3
    if n % 3 == 0:
        while n % 3 == 0:
            n //= 3
            t += 2
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
            t += 1
    if n != 1:
        print(-1)
    else:
        print(t)