for _ in range(int(input())):
    n = int(input())
    s = input()
    t = s.count('0')*1+s.count('1')*-1
    if t % 4 == 0: print('E')
    elif t % 4 == 1: print('S')
    elif t % 4 == 2: print('W')
    else: print('N')