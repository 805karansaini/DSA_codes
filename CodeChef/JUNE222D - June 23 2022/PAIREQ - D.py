from collections import defaultdict
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]

        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        
        k = max(dic.values())
        # print(k)

        print(n-k)
solve()