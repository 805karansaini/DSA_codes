from collections import defaultdict
def solve():
    t = int(input())
    while t:
        seen = {}
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()

        if n == 3:
            flag3 = False
            temp = sum(nums)
            for num in nums:
                if num == temp:
                    flag3 = True
                    break
            if flag3:
                print("YES")
            else:
                print("NO")
            continue
        
        dic = defaultdict(int)
        for variable in nums:
            dic[variable] += 1
        flag = True
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                templis = [a,nums[r],nums[l]]
                templis.sort()
                tempset = tuple(templis)
                if tempset in seen:
                    while nums[l] == nums[l-1] and l<r:
                            l+=1
                    continue
                else:
                    dic[a] -= 1
                    dic[nums[l]] -= 1
                    dic[nums[r]] -= 1
                    seen[tempset] = 1
                    temp = a+nums[r]+nums[l]
                    if dic[temp] < 1:
                        print("NO")
                        flag = False
                        break
                    else:
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
                        dic[a] += 1
                        dic[nums[l]] += 1
                        dic[nums[r]] += 1
            if flag==False:
                break
        if flag==False:
            continue
        else:
            for i,a in enumerate(nums):
                if i > 0 and a == nums[i-1]:
                    continue
                l,r = i+1, len(nums)-1
                while l<r:
                    templis = [a,nums[r],nums[l]]
                    templis.sort()
                    tempset = tuple(templis)
                    if tempset in seen:
                        while nums[r] == nums[r-1] and l<r:
                                r-=1
                        continue
                    else:
                        dic[a] -= 1
                        dic[nums[l]] -= 1
                        dic[nums[r]] -= 1
                        seen[tempset] = 1
                        temp = a+nums[r]+nums[l]
                        if dic[temp] < 1:
                            print("NO")
                            flag = False
                            break
                        else:
                            while nums[r] == nums[r-1] and l<r:
                                r-=1
                            dic[a] += 1
                            dic[nums[l]] += 1
                            dic[nums[r]] += 1
                if flag==False:
                    break
        if flag:
            print("YES")

solve()