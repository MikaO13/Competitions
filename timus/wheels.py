n = int(input())

wps = {}
tc = 0

for i in range(n):
    wheel = input()
    if wheel in wps:
        wps[wheel] += 1
    else:
        wps[wheel] = 1

for w in wps:
    tc += wps[w] // 4

print(tc)