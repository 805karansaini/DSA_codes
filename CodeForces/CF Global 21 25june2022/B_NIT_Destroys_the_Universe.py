def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        
        count = 0
        for c in nums:
            if c == 0:
                count += 1

        if count == n:
            print("0")
            continue
        elif count == 0:
            print("1")
        else:
            i = 0
            j = 0
            while i < n:
                if i == 0 and nums[i] == 0:
                    while nums[i] == 0:
                        i+=1
                        j+=1
                
                while i < n and nums[i] > 0

            if nums[0] == 0 and nums[n-1] == 0:
                count -= 1
            print(count)
    
solve()

#     res = 0
#         i = 0
#         while i < n:
#             while i < n and nums[i] == 0:
#                 i += 1
#             # print(nums[i], i, " ress ")
#             flag = False
#             while i < n and nums[i] > 0:
#                 i+=1
#                 flag = True
#             if flag:
#                 res += 1

#         i = 0
#         res1 = 0
#         if res > 1:
#             while i < n:
#                 if nums[i] == 0 and i == 0:
#                     while i < n and nums[i] == 0:
#                         i += 1
#                         pass
#                     # print(nums[i], i, " ress ")
                
#                 while i < n and nums[i] > 0:
#                     i+=1
#                 flag = False
#                 while i < n and nums[i] == 0:
#                     flag = True
#                     i += 1
#                 if flag:
#                     res1 += 1
#             final = min(res,res1+1)
#             print(final)
#         else:
#             print(res)
        
        