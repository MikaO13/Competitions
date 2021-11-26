n = int(input())

for i in range(n):
    w = input()
    length = len(w)
    if length <= 10:
        print(w)
    else:
        print(w[0] + str(length-2) + w[length - 1])
        