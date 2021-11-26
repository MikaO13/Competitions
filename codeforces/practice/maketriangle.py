s = [int(i) for i in input().split()]
ma = max(s[0], s[1], s[2])
s.remove(ma)
print(max(0, ma - (s[0] + s[1]) + 1))