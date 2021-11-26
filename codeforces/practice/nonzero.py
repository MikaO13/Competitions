for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    z = 0
    s = 0
    for i in a:
        s += i
        if i == 0: z += 1
    if z == 0 and s != 0:
        print(0)
    if z != 0:
        if s + z == 0:
            print(z + 1)
        else:
            print(z)
    elif s == 0:
        print(1)