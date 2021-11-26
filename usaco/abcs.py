for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    if n == 7:
        a, b = nums[0], nums[1]
        if nums[2] == a+b: c = nums[3]
        else: c = nums[2]
        sums = [a+b, a+c, b+c, a+b+c, c]
        good = True
        for i in range(2, 7):
            if nums[i] not in sums:
                good = False
                print(0)
                break
        if good: print(1)
    if n == 6:
        pass
    if n == 5:
        pass
    if n == 4:
        sols = []
        difs = [nums[1]-nums[0], nums[2]-nums[0], nums[3]-nums[0], nums[2]-nums[1], nums[3]-nums[1], nums[3]-nums[2]]
        total = difs+nums
        total.sort()
        for i in range(len(total)):
            a = total[i]
            
