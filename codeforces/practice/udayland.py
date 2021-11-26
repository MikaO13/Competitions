n = int(input())
s = []
f = "NO"
for i in range(n):
    s.append(input().split('|'))
for pair in s:
    if pair[0] == 'OO':
        pair[0] = '++'
        f = "YES"
        break
    elif pair[1] == 'OO':
        pair[1] = '++'
        f = "YES"
        break
print(f)
if f == "YES":
    for pair in s:
        print(pair[0] + '|' + pair[1])