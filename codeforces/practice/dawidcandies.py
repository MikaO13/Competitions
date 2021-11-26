a = [int(i) for i in input().split()]
a.sort()
s = "NO"
if a[3] == a[0] + a[1] + a[2]: s = "YES"
else:
    if a[3] + a[0] == a[1] + a[2]: s = "YES"
    elif a[3] + a[1] == a[0] + a[2]: s = "YES"
    elif a[3] + a[2] == a[1] + a[2]: s = "YES"
print(s)