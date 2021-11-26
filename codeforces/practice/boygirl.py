p = input()
chars = []
t = 0
for char in p:
    if char not in chars:
        chars.append(char)
        t += 1

if t % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")