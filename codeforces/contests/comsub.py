for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    s = set(a) & set(b)

    if len(s) >= 1:
        print('YES\n1', s.pop())
    else:
        print('NO')