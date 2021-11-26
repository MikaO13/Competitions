n = int(input())
s = [int(i) for i in input().split()]
a = ""
t = 0
for i in range(n):
    if s[i] == 1 and i != 0:
        t += 1
        a += str(s[i-1]) + " "
a += str(s[i]) + " "
print(t+1)
print(a[:-1])