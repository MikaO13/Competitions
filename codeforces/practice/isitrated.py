n = int(input())
a = []
b = []
s = "maybe"

for i in range(n):
    ai, bi = input().split()
    a.append(ai)
    b.append(bi)

for i in range(n):
    if a[i] != b[i]: 
        s = "rated"
        break
if s != "rated":
    for i in range(1, n):
        if int(a[i]) > int(a[i-1]): s = "unrated"
print(s)