n = int(input())
p = ["16", "06", "68", "88"]
if n <= 4:
    for i in range(n):
        if i != n:
            print(p[i], end = " ")
        else:
            print(p[i])
else:
    print("Glupenky Pierre")