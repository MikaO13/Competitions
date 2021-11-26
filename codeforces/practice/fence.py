n, h = map(int, input().split())
f = [int(i) for i in input().split()]
t = 0
for i in f:
    if i > h:
        t += 2
    else:
        t += 1
print(t)