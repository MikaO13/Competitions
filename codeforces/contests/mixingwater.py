for _ in range(int(input())):
    h, c, t = map(int, input().split())
    n = 0
    ct = 0
    if h == t: print(1)
    elif t <= (h+c)//2: print(2) 
    else:
        t -= (h+c)/2
        t1 = ((h-c)/2)/t
        x1 = int(((t1-1)//2)*2+1)
        x2 = int(((t1+1)//2)*2+1)
        if (h-c)/(x1*2)-t <= t - (h-c)/(x2*2): print(x1)
        else: print(x2)

        '''
        med = (h + c)/2
        last = (h+c+h)
        n = 3
        for i in range(20):
            print(t-((last)/(n)), t - (last + h + c)/(n+2))
            if abs(t-(last/n)) > abs(t - (last + h + c)/(n+2)):
                if abs(t-((last+h+h+c+c)/(n+4))) > abs(t - (last + h + c)/(n+2)):
                    print(n+2)
                    break
                else:
                    n += 2
                    last += h + c
            if abs(t-(last/n)) < abs(t - (last + h + c)/(n+2)):
                if abs(t-((last+h+h+c+c)/(n+4))) > abs(t - (last + h + c)/(n+2)):
                    print(n)
                    break
                else:
                    n += 2
                    last += h + c
            else:
                n += 2
                last += h + c
        '''