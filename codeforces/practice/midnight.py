n, k = map(int, input().split())

m = 0

for i in range(1, n + 2):
    m += i*5
    if m > 240-k:
        break
print(i - 1)