n, k = map(int, input().split())
a = [int(i) for i in input().split()]
d = []
ans = []
for i in range(n):
    if a[i] not in d: 
        d.append(a[i])
        ans.append(i+1)
if len(ans) >= k:
    print("YES")
    for i in range(k):
        print(ans[i], end = " ")
else:
    print("NO")