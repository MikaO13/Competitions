n, t = map(int, input().split())
qstr = input()
q = []
for i in range(n):
    q.append(qstr[i])
for j in range(t):
    i = 1
    while i < n:
        if q[i] == 'G' and q[i-1] == 'B':
            q[i] = 'B'
            q[i-1] = 'G'
            i += 1
        i += 1

print(''.join(q))