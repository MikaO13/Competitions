for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    s = "YES"
    for i in range(len(a)):
        if a[i] == c[i] or b[i] == c[i]:
            continue
        else:
            s = "NO"
    print(s)