l, r = map(int, input().split())
a = -1
for i in range(l, r+1):
    s = str(i)
    c = []
    t = True
    for char in s:
        if char in c:
            t = False
            break
        else:
            c.append(char)
    if t == False:
        pass
    else:
        a = i
        break
print(a)