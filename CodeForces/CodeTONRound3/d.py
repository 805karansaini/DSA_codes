from collections import Counter, defaultdict
import math

def solve():
    t = int(input())
    MOD = 998244353
    while t:
        t-=1
        n, m = [*map(int,input().split())]
        nums = [*map(int,input().split())]
        flag = True
        prev = nums[0]

        for temp in nums:
            if prev >= temp:
                prev = temp
            else:
                flag = False 
                break
        if flag == False:
            print("0")
            continue

        res = 1
        if nums[0]==1:
            for i in range(n-1):
                res = (res*m)%MOD
            print(res)
            continue
        factors = []
        breaaaaaaaaaak = 0
        for i in range(1,n):
            if nums[i] == 1:
                breaaaaaaaaaak = i
                for val in range(2,nums[i-1]+1):
                    if math.gcd(nums[i-1], val) != nums[i]:
                        factors.append(val)
                break
            else:
                res =  (res * (m//nums[i] - m//nums[i-1]) ) % MOD
        
        if i == n-1:
            print(res)
        tempTotalAdd = 0
        for c in factors:
            tempTotalAdd += m//c
        # print("TEMP : ", tempTotalAdd)
        allMulti = []
        for i in range(1,len(factors)):
            for j in range(0,i):
                allMulti.append(factors[i]*factors[j])
        for c in allMulti:
            tempTotalAdd -= m//c
        # print("TEMP : ", tempTotalAdd)
        res = (res * (m- tempTotalAdd))%MOD
        # print(res)
        for var in range(breaaaaaaaaaak+1,n):
            res = (res*m)%MOD
        print(res)
        # value = 0
        # breakedd = set()
        # seen = set()
        # for i in temp:
        #     breakedd = set()
        #     for v in range(i,1000, i):
        #         if v in seen:
        #             breakedd.add(v)
        #         seen.add(v)
        #     print(i, sorted(breakedd))
        # print(temp)

        # print(sorted(breakedd))
        # print(len(seen), len(breakedd),  len(seen) - len(breakedd))
        # # res = 1
        # # temp = (1000000000//30 - 1000000000//60)
        # # print(temp)
        # # res *= temp
        # # res *= (1000000000//1 - 1000000000//30)
        # # res *= 1000000000
        # # res = res%MOD
        # # print(res)
solve()