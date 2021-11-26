c, e = map(int, input().split())

v = []
for i in range(c):
    v.append(0)

for i in range(e):
    v[int(input())-1] +=1 

for can in v:
    print("{:0.2f}%".format(can*100/e))
