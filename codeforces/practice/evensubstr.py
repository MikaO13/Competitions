n = int(input())
s = input()
t = 0

for i in range(n):
    if int(s[i])%2==0: t+=i+1

print(t)