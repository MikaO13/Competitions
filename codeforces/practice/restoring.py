x1, x2, x3, x4 = map(int, input().split())

abc = 0
for i in [x1, x2, x3, x4]:
    if i > abc:
        abc = i
non = []
for i in [x1, x2, x3, x4]:
    if i != abc:
        non.append(i)

s = ""

for i in non:
    s += str(abc - i) + " "

print(s[:-1])