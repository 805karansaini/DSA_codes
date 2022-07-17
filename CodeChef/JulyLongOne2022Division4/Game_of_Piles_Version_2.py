import math

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        a = nums[0]
        b = nums[1]
        if a==b and a == 1:
            rem = 0
            for num in nums:
                if num > 1:
                    rem += num-1
            
            if rem%2 == 1:
                print("CHEF")
            else:
                print("CHEFINA")
            continue
        if a==1:
            rem = 0
            for num in nums:
                if num > 1:
                    rem += num-1
            if rem%2 == 1:
                print("CHEFINA")
            else:
                print("CHEF")
            continue
        else:
            temp = 0
            add = 0
            for num in nums:
                add += num - 1
            if add%2==1:
                print("CHEF")
            else:
                print("CHEFINA")


        # add, c1 = 0, 0
        # for num in nums:
        #     if num == 1:
        #         c1 += 1
        #     else:
        #         add += num-1

        # if add%2 == 0:
        #     print("CHEFINA")
        # else:
        #     print("CHEF")
      
solve()
