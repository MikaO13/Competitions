x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
t = a + b + c
if a >= x:
    a -= x
    t -= x
    if a + b >= y:
        t -= y
        if t >= z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")