n1 = int(input())
n2 = int(input())
n3 = int(input())

nums = [n1,n2,n3]

if n1 - n2 - n3 < n1 - (n2*n3):
    print(n1-n2-n3)
else:
    print(n1 - (n2*n3))