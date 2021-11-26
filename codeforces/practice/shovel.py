k, r = map(int, input().split())
i = 0
a = 0
while True:
    i += 1
    
    if (k*i-r)%10==0:
        a = i
        break
    elif (k*i)%10==0:
        a = i
        break
print(a)