a, b = map(int, input().split())
x = 0
if a <= b: x = a
else: x = b
a -= x
b -= x
y = a // 2 + b // 2
print(x, y)