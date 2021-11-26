n = int(input())
t = 0
if n > 1: 
    for num in range(1, n + 1):
        t += num
else:
    for num in range(n, 2):
        t += num
print(t)