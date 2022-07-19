tc = int(input())
for case in range(tc):
 
    n = int(input())
    a = list(map(int, input().split()))
 
    odd = [max(0, max(a[i-1], a[i+1])-a[i] + 1) for i in range(1,n-1,2)]
    mn = sum(odd)
    if n%2:
        print(mn)
    
    else:
        even = [max(0, max(a[i-1], a[i+1])-a[i] + 1) for i in range(2, n-1, 2)]
        cur = sum(even)
        mn = min(mn, cur)
 
        for i in range(n//2-1):
            cur += odd[i] - even[i]
            mn = min(mn, cur)
        
        print(mn)

# from collections import defaultdict
# import copy
# import heapq
# from re import I

# #NOT SOLVED
# def solve():
   
#     t = int(input())
#     while t:
#         t-=1
#         n = int(input())
#         nums = [*map(int,input().split())]
        
#         ansodd = 0
#         anseven = 0
#         maxi = (n-1)//2
#         tempmaxi = 0
#         # for odd values
#         if n%2 == 1:
#             while maxi != tempmaxi:
#                 for i in range(1,n-1,2):
#                     if nums[i-1] < nums[i] > nums[i+1]:
#                         tempmaxi += 1
#                         continue
#                     else:
#                         temp = max(nums[i-1],nums[i+1])
#                         ansodd = temp - nums[i] + 1
#                         tempmaxi += 1
#             print(ansodd)
#             continue
#         else:
#             ans = []
#             dic = defaultdict(int)
#             flag = [True] * n
#             for i in range(1,n-1):
#                 if nums[i-1] < nums[i] > nums[i+1]:
#                         dic[i] = 0
#                 else:
#                     temp = max(nums[i-1],nums[i+1])
#                     dic[i] = (temp - nums[i]) + 1
#             dic = dict(sorted(dic.items(), key=lambda item: item[1]))
#             print(dic)
#             anseven = 0
#             tempmaxi = 0
#             evenmaxi = (n-1)//2
#             for i,j in dic.items():
#                 if flag[i-1] == True and flag[i+1] == True:
#                     anseven += j
#                     tempmaxi += 1
#                     flag[i-1] = False
#                     flag[i+1] = False
#                     flag[i] = False
#                 print(tempmaxi,evenmaxi)
#                 if tempmaxi == evenmaxi:
#                     break
#             print(anseven, "even")
#         print()

# solve()