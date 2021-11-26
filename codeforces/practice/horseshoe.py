s = [i for i in input().split()]
h = []
t = 0
for i in s:
    if i in h:
        t += 1
    else:
        h.append(i)

print(t)