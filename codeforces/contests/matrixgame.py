for _ in range(int(input())):
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append([int(i) for i in input().split()])
    cc = [True for i in range(m)]
    cr = [True for i in range(n)]
    t = 0
    for row in range(n):
        for col in range(m):
            if b[row][col] == 1: 
                cc[col] = False
                cr[row] = False

    for i in range(n):
        for j in range(m):
            if cc[j] and cr[i]:
                t += 1
                cc[j] = False
                cr[i] = False
    if t % 2 == 0:
        print("Vivek")
    else:
        print("Ashish")