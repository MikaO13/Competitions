r, c = map(int, input().split())
cake = []
cc = [True for i in range(c)]
cr = [True for i in range(r)]
t = 0
for i in range(r):
    cake.append(input())
for row in range(r):
    for col in range(c):
        if cake[row][col] == 'S': 
            cc[col] = False
            cr[row] = False

for i in range(r):
    for j in range(c):
        if cc[j] or cr[i]:
            t += 1
print(t)