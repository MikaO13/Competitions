x, y = map(int, input().split())
p = []
c = "#Black&White"
for i in range(x):
    p.append([i for i in input().split()])
for i in p:
    for j in i:
        if j != "W" and j!= "B" and j != "G":
            c = "#Color"
            break
print(c)