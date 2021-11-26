n = int(input())
t = 0
for i in range(n):
    p, q = map(int, input().split())
    if p+2<=q:
        t +=1

print(t)