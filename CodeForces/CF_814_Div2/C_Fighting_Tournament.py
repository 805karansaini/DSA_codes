from collections import defaultdict, deque
import bisect

def solve():
    t = int(input())
 
    while t:
        t-=1
        n,q = [*map(int, input().split())]
        nums = [*map(int, input().split())]
        
        queries = []
        maxround = -1
        for i in range(q):
            idx, round = [*map(int, input().split())]
            maxround = (max(maxround, round))
            queries.append([idx, round])

        indxdic = defaultdict(int)

        for i,num in enumerate(nums):
            indxdic[i+1] = num

        dic = defaultdict(list)
        win = nums[0]

        for i in range(maxround):
            if win > nums[i+1]:
                dic[win].append(i+1)
            else:
                dic[nums[i+1]].append(i+1)
                win = nums[i+1]

            if win == n:
                breakround = i+1
                break
        for indx,rnd in queries:
            number = indxdic[indx]
            ans = bisect.bisect(dic[number], rnd)

            if number == n:
                if ans == 1:
                    ans = ans + (rnd-breakround)
                print(ans)
            else:
                print(ans)

solve()