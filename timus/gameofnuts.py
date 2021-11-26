n = int(input())

sps = [int(i) for i in input().split()]

total = 0

for pile in sps:
    if (pile - 1)//2 > 0:
        total += (pile - 1)//2

if total % 2 == 1:
    print("Daenerys")
else:
    print('Stannis')