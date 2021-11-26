n = int(input())
c = []
for i in range(n):
    c.append([int(i) for i in input().split()])
k = int(input())

for i in range(len(c)):
    if c[i][1] < k:
        continue
    else:
        print(n-i)
        break