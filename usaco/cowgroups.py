n = int(input())
ids = list(map(int, input().split()))
odd, even = 0, 0
for cow in ids:
    if cow % 2 == 0: even += 1
    else: odd += 1
c = 0
if odd > even:
    c += even*2
    odd -= even
    while odd >= 3:
        c += 2
        odd -= 3
    if odd == 2:
        c += 1
    elif odd == 1: 
        c -= 1
elif even > odd:
    c = odd*2 + 1
else: # even = odd
    c = odd*2

print(c)