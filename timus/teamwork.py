n = int(input())
nums = [int(i) for i in input().split()]

o = []
cn = -1
cc = 0

for i in nums:
    if i == cn:
        cc += 1
    else:
        if cn != -1:
            o.append(cc)
            o.append(cn)
        cc = 1
        cn = i

o.append(cc)
o.append(cn)

for i in o:
    if i != o[:-1]:
        print(i, end=' ')
    else:
        print(i)