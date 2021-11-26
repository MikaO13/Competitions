for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    a = []
    t = 0
    for i in range(n):
        a.append(input())
    for row in a:
        cnt = 0
        for char in row:
            if char == ".":
                cnt += 1
            else:
                if cnt >= 2:
                    if y < x*2:
                        t += (cnt//2)*y + (cnt%2)*x
                    else:
                        t += cnt*x
                else: 
                    if cnt > 0: t += x
                cnt = 0
        if cnt >= 2:
            if y < x*2:
                t += (cnt//2)*y + (cnt%2)*x
            else:
                t += cnt*x
        else: 
            if cnt > 0: t += x
    print(t)