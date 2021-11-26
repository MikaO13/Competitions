for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    t = [True] * n
    c = 0
    for i in range(n):
        if s[i] == "1":
            for j in range(i-k, i+k+1):
                if j >= 0 and j < n:
                    t[j] = False
    
    for i in range(n):
        if t[i] == True:
            c += 1
            for j in range(i-k, i+k+1):
                if j >= 0 and j < n:
                    t[j] = False
    print(c)