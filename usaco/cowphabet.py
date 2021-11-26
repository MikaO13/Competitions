a = input()
s = input()
c = 0
num = 26
for char in s:
    #print(char)
    #print(c)
    if num >= a.index(char):
        c += 1
    num = a.index(char)
print(c)