n = int(input())
t = 0
for i in range(1, n):
    if (n-i) % i == 0: t += 1
print(t)