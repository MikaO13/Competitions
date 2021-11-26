n, m, y = map(int, input().split())
nums = []

for x in range(0, m):
    if x ** n % m == y:
        nums.append(x)

if nums != []:
    topr = ""
    for num in nums:
        topr += str(num) + " "

    print(topr[:-1])
else:
    print("-1")