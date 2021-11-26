a, b, c = map(int, input().split())
print(min(a+b+c, 2*a+2*b, 2*a+2*c, 2*b+2*c))