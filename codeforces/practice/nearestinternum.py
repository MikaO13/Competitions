n = input()
s = 0
for i in n:
    s += int(i)
while s % 4 != 0:
    n = str(int(n) + 1)
    s = 0
    for i in n:
        s += int(i)
print(n)