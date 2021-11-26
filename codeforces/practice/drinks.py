n = int(input())
p = [int(i) for i in input().split()]
t = 0
for i in p:
    t += i/n
print(round(t, 15))