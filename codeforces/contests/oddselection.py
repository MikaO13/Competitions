for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    o, e = 0, 0
    s = 0
    for i in a: 
        if i%2==0: e += 1
        else: o += 1
        s += i
    if s%2!=0 or s==1:
        print("YES")
    else:
        if o != 0 and e != 0:
            print("YES")
        else:
            print("NO")