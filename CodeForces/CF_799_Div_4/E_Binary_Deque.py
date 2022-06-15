import sys, math, itertools, functools, collections
input = sys.stdin.readline
 
for testcase in range(int(input())):
    n, s = map(int, input().split())
    a = [*map(int, input().split())]
    if sum(a) < s:
        print('-1')
        continue
    best = -10**18
    d = [0]
    cur = 0


    for i in range(1, n+1):
        cur += a[i-1]
        print(curr, " : curr")
        if cur >= len(d):
            d.append(i)
            print(d, " : d")
        if cur >= s:
            print(best, (i - d[cur-s]), "best")
            best = max(best, i - d[cur-s])
    print(n-best)

# def solve():
#     t = int(input())

#     while t:
#         t-=1
#         n, target = [*map(int,(input().split()))]
#         nums = [*map(int,input().split())]
#         index = []
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 index.append(i)
            
#         lo, hi = 0, len(nums)-1
#         low, high = 0, len(index)-1
#         if target > len(index):
#             print("-1")
#         elif target == len(index):
#             print("0")
#         else:
#             c = 0
#             # print(index)
#             while abs(low-high)+1 != target:
#                 if abs(index[low] - lo)  <= abs(hi - index[high]):
#                     c += abs(index[low] - lo) + 1
#                     lo = index[low] + 1
#                     low += 1
#                     # print(c, low, " : ", lo, "", high, ":" if  : c")
#                 else:
#                     c += abs(hi - index[high]) + 1
#                     hi = index[high] - 1 
#                     high -= 1
#                     # print(c, low, high," if  : c")
#             print(c)  
#     return
# solve()