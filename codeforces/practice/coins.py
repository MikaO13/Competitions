t = int(input())

for i in range(t):
    n = [int(i) for i in input().split()]
    if (n[0] + n[1] + n[2] + n[3]) % 3 == 0:
        ma = 0
        for i in [n[1], n[2], n[0]]:
            if i > ma:
                ma = i
        dif = 0
        for i in [n[1], n[2], n[0]]:
            dif += ma - i 

        if n[3] >= dif:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        