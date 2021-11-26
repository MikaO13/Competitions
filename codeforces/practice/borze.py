s = input()
cnt = 0
a = ""
while cnt < len(s):
    if s[cnt] == '.':
        cnt -= 1
        a += "0"
    elif s[cnt+1] == '.':
        a += "1"
    else:
        a += "2"
    cnt += 2
print(a)