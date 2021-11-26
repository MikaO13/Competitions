n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    if a[i]%2==0: a[i]=a[i]-1
for i in range(n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i], end = " ")