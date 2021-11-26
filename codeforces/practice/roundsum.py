t = int(input())

for i in range(t):
    n = input()
    r = []
    for j in range(len(n)):
        if j == 0:
            r.append(n[j] + ("0"*(len(n) - 1)))
        else:
            if n[j] != "0":
                r.append(n[j] + ("0"*(len(n) - 1 - j)))
    print(len(r))
    for i in range(len(r)):
        if i == len(r) - 1:
            print(r[i])
        else:
            print(r[i], end = " ")