n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]
ma = 0
mb = 0
for i in a:
    ma = max(ma, i)
for i in b:
    mb = max(mb, i)
print(ma, mb)