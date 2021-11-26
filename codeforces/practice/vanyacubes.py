n = int(input())
x = 1
s = 0
c = 0
while True:
    for i in range(1, x + 1):
        s += i
    x += 1
    if s > n:
        break
    c += 1
print(c)