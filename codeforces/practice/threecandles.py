for _ in range(int(input())):
    p = [int(i) for i in input().split()]
    third = max(p[0], p[1], p[2])
    p.remove(third)
    if third > p[0] + p[1] or third > max(p[0], p[1]) - min(p[0], p[1]):
        print((p[0]+p[1]+third)//2)
    else:
        print(min(p[0]-p[1])+third)