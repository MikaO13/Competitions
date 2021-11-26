k2, k3, k5, k6 = map(int, input().split())
print(256*min(k2, k5, k6)+32*min(k2-min(k2,k5,k6), k3))
