n = int(input())
s = input()
cc = 0
t = 0

for char in s:
    if char == 'x':
        cc += 1
    else:
        if cc >= 3:
            t += cc - 2
        cc = 0
if cc >= 3:
    t += cc - 2
print(t)