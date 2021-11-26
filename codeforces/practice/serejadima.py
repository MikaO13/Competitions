n = int(input())
c = [int(i) for i in input().split()]
s = 0
d = 0
while len(c) > 0:
    if c[0] > c[len(c)-1]:
        s += c[0]
        c.pop(0)
    else:
        s += c[len(c)-1]
        c.pop(len(c)-1)
    if len(c) <= 0:
        break
    else:
        if c[0] > c[len(c)-1]:
            d += c[0]
            c.pop(0)
        else:
            d += c[len(c)-1]
            c.pop(len(c)-1)
print(s, d)