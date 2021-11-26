n = int(input())

f = n // 1000
l = n % 1000

def toSum(n):
    return n//100 + n//10%10 + n%10

sf = toSum(f)

if toSum(l + 1) == sf or toSum(l - 1) == sf:
    print("Yes")
else:
    print("No")