n = int(input())
a = [int(i) for i in input().split()]
a.sort()
l = 0
c = 0
ma = 0
for i in a:
    if i == l:
        c += 1
    else:
        ma = max(ma, c)
        c = 1
    l = i
ma = max(ma, c)
print(ma)