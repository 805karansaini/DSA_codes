from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [1,2,3,4,5,6,7,8,9]
        res = []
        flag = False
        def comb(p, up,total,i):
            if len(p)==k and total == n:
                res.append(p[:])
                return
            if len(p) >= k:
                return
            for j in range(i, len(nums)):
                if total + nums[j] > n:
                    break
                p.append(nums[j])
                total += nums[j]
                comb(p,up,total, j + 1)
                p.pop()
                total -= nums[j]

        for i in range(1,10):
            k = i
            comb([],nums,0, 0)
        print( "".join(map(str,res[0])) )
solve()# cook your dish here
