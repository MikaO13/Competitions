cpm, m = map(int, input().split())
cars = [int(i) for i in input().split()]
lc = 0
#nc = 0
#for car in cars:
#    nc += car

#if (nc-(cpm*m)) < 0:
#    print(0)
#else:
#    print(nc - (cpm*m))

for minute in range(m):
    if cars[minute] > cpm:
        lc += cars[minute] - cpm
    else: 
        lc -= cpm - cars[minute]
        if lc < 0: lc = 0

if lc < 0:
    print(0)
else:
    print(lc)