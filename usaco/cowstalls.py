import math
n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

stalls.sort(reverse = True)
cows.sort(reverse = True)

t = 0
ts = len(stalls)
m = [] # storage for to multiply total by
for cow in cows:
    c = 0
    for stall in stalls: 
        if cow <= stall: c += 1
        else: break
    c -= (len(stalls) - ts)
    #print(c)
    if c == ts:
        t = math.factorial(c)
        break
    else:
        m.append(c)
        ts -= 1

for num in m:
    t *= num

print(t)