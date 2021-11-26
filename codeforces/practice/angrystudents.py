for _ in range(int(input())):
    n = int(input())
    s = input()
    ma = 0
    ps = 0
    a = False
    for i in range(n):
        if a == True and s[i] == "P":
            ps += 1
        elif s[i] == "A":
            ma = max(ma, ps)
            ps = 0
            a = True
    ma = max(ma, ps)
    print(ma)