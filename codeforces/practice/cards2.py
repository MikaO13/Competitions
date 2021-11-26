n = int(input())
c = [int(i) for i in input().split()]
g = 0
for i in c:
    g += i
g = g // (n//2)
for i in range(n):
    for j in range(i+1, n):
        if c[i] + c[j] == g:
            print(i+1, j+1)
            c[i] = -1
            c[j] = -1
            break
