def solve():
    t = int(input())
    while t:
        t-=1
        n , z = [*map(int,input().split())]
        nums = [*map(int,input().split())]
        # nums.sort()
        best = -10**20
        temp_nums = [0]*n
        m = 0
        for i,num in enumerate(nums):
            if num > m:
                m = num
            p = num | z
            temp_nums[i] = p
        high = m
        for i in range(n):
            if temp_nums[i] > high:
                high = temp_nums[i]
        
        print(high)

solve()
        # flag = True
        # count = 0
        # while flag and z > 0 and count < 3:
        #     if z == 0:
        #         count += 1
        #     flag = False
        #     for i in range(n-1,-1,-1):
        #         # print(nums[i])
        #         if nums[i] == 0:
        #             continue
        #         else:
        #             temp = nums[i] | z
        #             # print(temp, ": temp")
        #             if temp >= best:
        #                 flag = True
        #                 best = max(temp,best)
        #             z = nums[i] & z
        #             # print(z," : z")
        #             # print( best , z)
        # print(best, "best 1")
        # while flag and z > 0 and count < 3:
        #     if z == 0:
        #         count += 1
        #     flag = False
        #     for i in range(n):
        #         # print(nums[i])
        #         if nums[i] == 0:
        #             continue
        #         else:
        #             temp = nums[i] | z
        #             # print(temp, ": temp")
        #             if temp >= best:
        #                 flag = True
        #                 best = max(temp,best)
        #             z = nums[i] & z
        #             # print(z," : z")
        #             # print( best , z)
        # print(best, "Final best1")
