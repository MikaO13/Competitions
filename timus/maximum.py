n = -1

while n != 0:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        maxx = 1
    else:
        n = n + 1
        nums = [0, 1]
        maxx = 0
        for i in range(2, n):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[(i - 1) // 2] + nums[((i - 1) // 2) + 1])
            if nums[i] > maxx:
                maxx = nums[i]
    print(maxx)