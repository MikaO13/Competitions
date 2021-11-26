n = int(input())
s = input()
k = 0
a = ""
c = 0
for i in s:
    if i == "B":
        c += 1
    else:
        if c > 0: 
            k += 1
            a += str(c) + " "
            c = 0
if i == "B":
    k += 1
    a += str(c) + ' '
print(k)
if k > 0:
    print(a[:-1])