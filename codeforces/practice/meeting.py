h = [int(i) for i in input().split()]

if h[0] > h[1]: h[1], h[0] = h[0], h[1]
if h[1] > h[2]: h[1], h[2] = h[2], h[1]
if h[0] > h[1]: h[1], h[0] = h[0], h[1]

print(abs(h[0] - h[1]) + (h[2] - h[1]))