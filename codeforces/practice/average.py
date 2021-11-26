s = input()
s = s.replace(' ', '')
s = s.split(',')
for i in range(len(s)): 
    s[i] = int(s[i])
print(sum(s))
print(len(s))