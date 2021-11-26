n = int(input())

p = [0, 0, 0] #emp, mac, little

for i in range(n):
    cp = input()
    if cp == "Emperor Penguin":
        p[0] += 1
    elif cp == "Little Penguin":
        p[2] += 1
    else:
        p[1] += 1

if p[0] > p[1]:
    if p[0] > p[2]:
        print("Emperor Penguin")
    else:
        print("Little Penguin")
else:
    if p[1] > p[2]:
        print("Macaroni Penguin")
    else:
        print("Little Penguin")