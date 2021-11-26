n = int(input())
while True:
    n += 1
    if str(n)[0] == str(n)[1] or str(n)[0] == str(n)[2] or str(n)[0] == str(n)[3] or str(n)[1] == str(n)[2] or str(n)[1] == str(n)[3] or str(n)[2] == str(n)[3]:
        continue
    else:
        break
print(n)