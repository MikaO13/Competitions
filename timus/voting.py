import math
n = int(input())

groups = [int(i) for i in input().split()]

if n%2 == 0: gn = n // 2 + 1
else: gn = math.ceil(n/2)

total = 0

for r in range(n-1):
    for b in range(n-1-r):
        if groups[b] > groups[b + 1]:
            groups[b], groups[b + 1] = groups[b + 1], groups[b]

for i in range(0, gn):
    group = groups[i]
    if group%2 ==0: total += group //2 + 1
    else: total += math.ceil(group/2)

print(total)