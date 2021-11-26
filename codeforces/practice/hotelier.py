n = int(input())
s = input()
r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    if s[i] == "L":
        for i in range(10):
            if r[i] == 0:
                r[i] = 1
                break
    elif s[i] == "R":
        for i in range(9, -1, -1):
            if r[i] == 0:
                r[i] = 1
                break
    else:
        r[int(s[i])] = 0
for i in r: print(i, end = "")