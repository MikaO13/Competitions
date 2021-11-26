for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    sa = []
    for i in a:
        sa.append(i)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                if b[j] != b[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    b[j], b[j+1] = b[j+1], b[j]
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                if b[j] != b[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    b[j], b[j+1] = b[j+1], b[j]
    sa.sort()
    if sa == a:
        print("Yes")
    else:
        print("No")