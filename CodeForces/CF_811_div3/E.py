from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]        
        nums = list(set(nums))
        nums.sort()
        for i,n in enumerate(nums[:-1]):
            prev = -1
            flag = False
            temp = n
            while temp < nums[i+1]:
                temp = temp + (temp%10)
                if temp==nums[i+1]:
                    print(" break ans")
                    break
                if temp>nums[i+1]:
                    print(" temp > nums")
                    flag = True
                    break
                if prev==temp:
                    print(" prev number")
                    flag = True
                    break
                prev = temp
            if flag:
                print("NO")
                break
        if not flag:
            print("YES")
solve()# cook your dish here
