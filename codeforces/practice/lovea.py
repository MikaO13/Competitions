s = input()
n = len(s)
c = 0
for i in range(n):
    if s[i] == 'a':
        c += 1
while True:
    m = n//2+1
    if c >= m: break
    n -= 1
print(n)