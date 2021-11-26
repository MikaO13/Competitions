n = int(input())

t = 0
s = False
for i in range(n):
    g = int(input())
    t += g
    if g == 3 or g == 3.0:
        s = True

av = t / n

if s:
    print("None")
elif av >= 5.0:
    print("Named")
elif av >= 4.5:
    print("High")
else:
    print("Common")