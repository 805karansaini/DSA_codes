from collections import defaultdict
import copy
def solve():
    t = int(input())
    while t:
        t-=1
        n, k = [*map(int,input().split())]
        # print(n ,  k)
        nums = [*map(int,input().split())]
        sorted = copy.deepcopy(nums)
        sorted.sort()
        lim = sorted[-1] + sorted[-2]
        if nums == sorted:
            print("YES")
        elif k >= lim:
            print("YES")
        else:
            preCheck = True
            for i in range(n-1,-1,-1):
                if sorted[i] == nums[i]:
                    lim = sorted[i-1] + sorted[i-2]
                    if lim <= k:
                        print("YES")
                        preCheck = False
                        break
                else:
                    pointer = i
                    high = nums[i]
                    break

            if preCheck == False:
                pass
            else:
                flag2 = True
                flag = False
                index = None
                for i in range(pointer,-1,-1):
                    if nums[i] == high:
                        flag = True
                        continue
                    if nums[i] < high:
                        continue
                    else:
                        if nums[i] + high <= k:
                            high = max(high,nums[i])
                            index = i
                        else:
                            print("NO")
                            flag = False
                            flag2 = False
                            break
                high = nums[0]
                if flag:
                    for i in range(1,pointer+1):
                        if  high <= nums[i]:
                            high = max(high,nums[i])
                            continue
                        else:
                            if nums[i] + high <= k:
                                pass
                            else:
                                print("NO")
                                break
                    else:
                        print("YES")
                else:
                    if flag2:
                        print("YES")
solve()