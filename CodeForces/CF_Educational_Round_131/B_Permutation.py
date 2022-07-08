tc = int(input())
for case in range(tc):
 
    n = int(input())
    ans = []
 
    frsh = [True for i in range(n+1)]
 
    i = 1
    while i <= n:
        j = i
        while j <= n and frsh[j]:
            frsh[j] = False
            ans.append(j)
            j += j
        i+=1
        print(i)
    
    # print(2)
    # print(*ans)
# from copy import deepcopy
# import copy
# from typing import Counter


# def solve():
#     t = int(input())
#     while t:
#         t-=1
#         n = int(input())

#         # d = 2
        
#         d2 = 0
#         nums2 = [1]
#         dic2 = set()
#         dic2.add(1)
#         temp = 1
#         while temp <= n:
#             temp = temp * 2
#             if temp <= n and temp not in dic2:
#                 d2 +=1
#                 nums2.append(temp)
#                 dic2.add(temp)
#             else:
#                 for i in range(1,n+1):
#                     if i not in dic2:
#                         nums2.append(i)
#                         dic2.add(i)
#                         temp = i
#                         break
#                 if temp*2 > n:
#                     break
#         if n > 4:
#             print("2")
#             for i in range(1,n+1):
#                 if i not in dic2:
#                     nums2.append(i)
#             print(" ".join(map(str,nums2)))
#             continue
#         # d = 3

#         d3 = 0
#         nums3 = [1]
#         dic3 = set()
#         dic3.add(1)
#         temp = 1
#         while temp <= n:
#             temp = temp * 3
#             if temp <= n and temp not in dic3:
#                 d3 +=1
#                 nums3.append(temp)
#                 dic3.add(temp)
#             else:
#                 for i in range(1,n+1):
#                     if i not in dic3:
#                         nums3.append(i)
#                         dic3.add(i)
#                         temp = i
#                         break
                
#                 if temp*3 > n:
#                     break
#         if d3 >= d2:
#             print("3")
#             for i in range(1,n+1):
#                 if i not in dic3:
#                     nums3.append(i)
#             print(" ".join(map(str,nums3)))
        
#         else:
#             print("2")
#             for i in range(1,n+1):
#                 if i not in dic2:
#                     nums2.append(i)
#             print(" ".join(map(str,nums2)))
        
#         dic2.clear()
#         dic3.clear()
#         # dic = set()
#         # nums = [1]
#         # d = 2
#         # curr = 0
#         # ans = -1
#         # finald = 2
#         # while curr >= ans:
#         #     ans = curr
#         #     curr = 0
#         #     dic.add(1)
#         #     temp = 1
#         #     flag = True
#         #     while flag:
#         #         while temp <= n:
#         #             temp = temp * d
#         #             if temp <= n and temp not in nums:
#         #                 curr += 1
#         #                 nums.append(temp)
#         #                 dic.add(temp)
#         #         for var in range(1,n+1):
#         #             if var not in nums:
#         #                 var = var
#         #                 break
#         #         if temp == var:
#         #             flag = False
#         #             break
#         #         temp = var

#         #     if curr >= ans:
#         #         finald = d
#         #         numsans = copy.deepcopy(nums)
#         #     nums = [1]
#         #     d += 1
#         #     dic.clear()
#         #     dic.add(1)
#         # dicset = set(numsans)
#         # for i in range(1,n+1):
#         #         if i not in dicset:
#         #             numsans.append(i)
#         # print(finald)
#         # print(" ".join(map(str,numsans)))
        
# solve()