n = int(input())
p = [int(i) for i in input().split()]
y = "NO"

for i in range(n):
    if i == p[p[p[i - 1] - 1] - 1]:
        y = "YES"
        break
    
print(y)