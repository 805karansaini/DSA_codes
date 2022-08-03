from collections import Counter, defaultdict
import math
def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums = [ i+1 for i in range(N)]
        if N == 3:
            print(" ". join(map(str,nums)))
            continue
        ans = []
        ans.append(N)
        ans.append(N-2)
        for i in range(1,N-3):
            ans.append(i)
        ans.append(N-3)
        ans.append(N-1)
        print(" ". join(map(str,ans)))


        
        # j = 1
        # l = N
        # temp = N%3
        # if temp == 2:
        #     k = math.ceil(N/3) + 1
        # else: 
        #     k = math.floor(N/3) + 1
        # nums = [-1]*N
        # for i in range(N):
        #     if i%3 == 0:
        #         nums[i] = l
        #         l-= 1
        #     if i%3==1:
        #         nums[i] = j
        #         j+=1
        #     if i%3 == 2:
        #         nums[i] = k
        #         k+=1
            
        # print(" ". join(map(str,nums)))
        # print(sorted(Counter(nums)))



        # ans = [-1]*N
        # r, l = 0, -1
        # flag, c = True, 0
        # neg = -1
        # posi = 0
        # for i in range(N):
        #     if flag:
        #         if i%2==0:
        #             ans[r] = nums[neg]
        #             r+=1
        #         else:
        #             ans[l] = nums[neg]
        #             l-=1
        #         c += 1
        #         neg -=1
        #         if c == 2:
        #             flag = False
        #             c = 0
        #     else:
        #         if i%2==0:
        #             ans[r] = nums[posi]
        #             r+=1
        #         else:
        #             ans[l] = nums[posi]
        #             l-=1
        #         c += 1
        #         posi += 1
        #         if c == 4:
        #             flag = True
        #             c = 0
        # print(" ". join(map(str,ans)))
solve()# cook your dish here
