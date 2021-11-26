n = input()
t = 0
for char in n:
    if char == "7" or char == "4":
        t += 1
if t == 7 or t == 4:
    print("YES")
else:
    print("NO")