n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
x.pop(0)
y.pop(0)

l = [False for i in range(n)]
for i in x:
    l[i-1] = True
for i in y:
    l[i-1] = True

if False in l:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")