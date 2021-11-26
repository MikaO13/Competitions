a, b = input().split()

n = int(a)
k = len(b)

i = 0
t = 1
if n%k == 0:
    while True:
        tbc = (n - (i*k))
        if tbc == k:
            t *= tbc
            break
        else:
            t *= tbc
        i += 1
else:
    while True:
        tbc = (n - (i*k))
        if tbc == n%k:
            t *= tbc
            break
        else:
            t *= tbc
        i += 1

print(t)