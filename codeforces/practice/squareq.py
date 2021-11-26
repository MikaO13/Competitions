for _ in range(int(input())):
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    a = "No"
    if l1[1] <= 0 or l2[1] <= 0:
        continue
    else:
        for i in l1:
            for j in l2:
                if i == j:
                    l1.remove(i)
                    l2.remove(j)
                    if l1[0] + l2[0] == i: 
                        a = "Yes"
                        break
                    l1.append(i)
                    l2.append(j)
    print(a)