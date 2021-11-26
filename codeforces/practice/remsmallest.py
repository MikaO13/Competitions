for _ in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    if list(range(a[0], a[-1]+1)) == a:
        print('YES')
    else:
        print('NO')