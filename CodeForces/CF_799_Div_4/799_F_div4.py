from collections import defaultdict
def solve():
    t = int(input())
 
    while t:
        t-=1
        n = int(input())
        nums = [*map(int, input().split())]
        
        dic = defaultdict(int)
        for i in nums:
            dic[i%10] += 1
        # print(dic)
        res = "NO"
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if (i+j+k)%10 == 3:
                        dic[i] -= 1
                        dic[j] -= 1
                        dic[k] -= 1
                        if dic[i] >= 0 and dic[j] >= 0 and dic[k] >= 0:
                            res = "YES"
                        dic[i] += 1
                        dic[j] += 1
                        dic[k] += 1
        print(res)

    return 
solve()