def solve():
    t = int(input())

    while t:
        # print(t)
        t-=1
        n = int(input())
        if n < 2:
            num = input()
            print("-1")
        else:
            nums = input().split()
            nums = [int(i) for i in nums]
            temp = []
            res = []

            # print("hello WorldNEW")

            for i in range(1,n+1):
                if temp:
                    res.append(temp[0])
                    temp.pop(0)
                else:
                    if nums[i - 1] == i:
                        res.append(i+1)
                        temp.append(i)
                    else:
                        res.append(i)
            # print(temp, "temp")
            if temp:
                tmp = res[-2]
                res[-1] = tmp
                res[-2] = temp[0]
            print(' '.join(map(str, res)))
    return
solve()