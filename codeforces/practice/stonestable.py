n = int(input())
s = input()
t = 0
last = ""
for i in s:
    if i == last:
        t += 1
    else:
        last = i
print(t)