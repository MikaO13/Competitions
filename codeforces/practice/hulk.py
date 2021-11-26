n = int(input())

f = ""
for i in range(n):
    if i != n-1:
        if i%2==0: f += "I hate that "
        else: f += "I love that "
    else:
        if i%2==0: f += "I hate it"
        else: f += "I love it"

print(f)