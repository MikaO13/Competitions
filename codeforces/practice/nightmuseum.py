word = input()
lc = 'a'
t = 0
for c in word:
    x = max(ord(c)-ord('a')+1, ord(lc)-ord('a')+1)
    y = min(ord(c)-ord('a')+1, ord(lc)-ord('a')+1)
    if x - y <= 13:
        t += x-y
    else:
        t += 26 + y-x
    lc = c
print(t)