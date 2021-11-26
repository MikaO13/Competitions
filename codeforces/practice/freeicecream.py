n, x = map(int, input().split())
t = 0
for i in range(n):
    sign, num = map(str, input().split())
    if sign == '+': x += int(num)
    else:
        if int(num) > x:
            t += 1
        else:
            x -= int(num)
print(x, t)