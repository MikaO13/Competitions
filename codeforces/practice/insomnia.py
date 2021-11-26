k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
t = 0
for i in range(1, d+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        t+=1
print(t)