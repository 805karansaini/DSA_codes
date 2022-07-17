import math

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        
        mini = min(nums)
        if mini == 1:
            print("CHEF")
            continue
        else:
            rem = 0
            for num in nums:
                rem += num-2
            
            if rem%2 == 1:
                print("CHEF")
            else:
                print("CHEFINA")
  
solve()