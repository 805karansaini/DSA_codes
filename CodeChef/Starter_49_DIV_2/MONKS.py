# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict
import bisect
import math

def solve():
    def celling(nums, target):
            start = 0
            last = len(nums)-1
            temp = -1
        
            while start <= last:
                mid = (start + (last - start) // 2)
                if target > nums[mid]:
                    start = mid+1
                elif target < nums[mid]:
                    last = mid-1
                elif target == nums[mid]:
                    temp = mid
                    start= mid +1
            return temp;
    
 
        def floor(nums, target):
            start = 0
            last = len(nums)-1
            temp = -1
            while start <= last:
                mid = (start + (last - start) // 2)
            
                if target > nums[mid]:
                    start = mid+1
                elif target < nums[mid]:
                    last = mid-1
                elif target == nums[mid]:
                    temp = mid
                    last= mid - 1
            return temp;
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums=  [*map(int,input().split())]
        nums.sort()
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        
        if len(dic) == 1:
            print("0")
            continue

        summ = sum(nums)
        temp1 = math.ceil(summ / n)
        temp2 = math.floor(summ / n)
        for i, j in dic.items()
            mode = j
            break
        
        # C-1 for mode
        left = bisect.bisect_left(nums, mode)
        right = bisect.bisect_rightt(nums, mode,0, n)
        if abs( mode*left - sum(nums[:left]) ) <=   sum(nums[right:]):
            ans1 = n-right
        elif abs( mode*left - sum(nums[:left]) ) >   sum(nums[right:]):
            

        for i in range(n-1,0,-1):
            ans += 1
            var = nums[i]
            # summ -= var
            dic[var] -= 1
            if dic[var] == 0:
                del dic[var]
                if len(dic)==1:
                    print(ans)
                    break

            if summ//i+1 == temp1 or summ//i+1 == temp2 :
                print(ans)
                break



solve()# cook your dish here
