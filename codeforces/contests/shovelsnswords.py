for _ in range(int(input())):
    a, b = map(int, input().split())
    t = 0
    #t += min(max(a, b)//2, min(a, b))
    print(min((a+b)//3, min(a,b)))