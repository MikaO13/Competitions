n = int(input())
t = 0
for i in [100, 20, 10, 5, 1]:
    t += n // i
    n = n % i
print(t)
