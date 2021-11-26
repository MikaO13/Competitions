n, m = map(int, input().split())
s = [i for i in input().split()]
t = [i for i in input().split()]

for _ in range(int(input())):
    #find the mapped thing
    y = int(input())
    print(s[(y-1)%n]+t[(y-1)%m])
