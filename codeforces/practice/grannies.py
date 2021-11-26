t = int(input())

for test in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    gran = {}
    for i in a:
        if i in gran:
            gran[i] += 1
        else:
            gran[i] = 1
    t = 1
    for g in gran:
        if gran[g] != 0:
            maybe = t
            maybelst = []
            for may in gran:
                if may < g and gran[may] != 0:
                    maybe += gran[may]
                    maybelst.append(may)
            if maybe + gran[g] > g:
                t += maybe + gran[g] - t
                gran[g] = 0
                for may in maybelst:
                    gran[may] = 0
    print(t)