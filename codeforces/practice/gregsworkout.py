n = int(input())
a = [int(i) for i in input().split()]
c = [0, 0, 0]
for i in range(n):
    c[(i+1)%3-1] += a[i]
if c[0] > c[1] and c[0] > c[2]: print("chest")
elif c[1] > c[0] and c[1] > c[2]: print("biceps")
else: print("back")