import math
n = int(input())
#t = 0
#for i in range(1, n+1):
#    t += i*((-1)**i)
#print(t)
if n%2==0: print(n//2)
else: print(math.ceil(n/2) * -1)