n = int(input())
c = [int(i) for i in input().split()]
p = 0
t = 0

for i in c:
    if i == -1:
        if p == 0:
            t += 1
        else:
            p -= 1
    else:
        p += i

print(t)