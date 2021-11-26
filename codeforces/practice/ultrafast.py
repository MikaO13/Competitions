a = input()
b = input()
n = len(a)
s = ""
for i in range(n):
    if a[i] == b[i]: s += "0"
    else: s += '1'
print(s)