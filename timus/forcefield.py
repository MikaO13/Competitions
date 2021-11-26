n = int(input())
ff = [int(i) for i in input().split()]

mn = 0
mi = 0

for i in range(n-2):
    t = ff[i] + ff[i+1] + ff[i+2]
    if t > mn:
        mn = t
        mi = i

print(str(mn) + ' ' + str(mi + 2))