c = input()
h = [i for i in input().split()]
t = "NO"
for i in h:
    if i[0] == c[0] or i[1] == c[1]:
        t = "YES"
        break
print(t)