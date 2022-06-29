from collections import defaultdict
import math
 
def solve():

    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        dic = defaultdict(int)
        even_list = []
        EPZ = []
        for num in nums:
            if (num%2)==0:
                dic["even"] += 1
                if (num & (num-1) == 0) and num != 0:
                    EPZ.append(num)
                else:
                    even_list.append(num)
            else:
                dic["odd"] += 1
        # print(dic["odd"], dic["even"], even_list, EPZ)
        if dic["odd"] == dic["even"]:
            print("0")
        elif dic["odd"] > dic["even"]:
            ans = dic["odd"] - dic["even"]
            ans = ans // 2
            print(ans)
            continue
        elif dic["odd"] < dic["even"]:
            if len(even_list) >= (dic["even"] - dic["odd"])//2:
                ans = dic["even"] - dic["odd"]
                ans = ans//2
                print(ans)
            else:
                ans = (dic["even"] - dic["odd"])//2
                ans = ans - len(even_list)
                c = len(even_list)
                EPZ.sort()
                for nz in EPZ:
                    tempcount = 0
                    while nz%2==0:
                        nz = nz//2
                        tempcount += 1
                    if ans > 0:
                        c += tempcount
                        ans-=1
                    if ans < 1:
                        break
                print(c)

solve()