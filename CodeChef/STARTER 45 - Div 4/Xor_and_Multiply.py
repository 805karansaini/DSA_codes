from collections import defaultdict
import math
from re import M
from unicodedata import decimal
 
def solve():

    def binatodeci(binary):
        return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

    t = int(input())
    while t:
        t-=1
        n, a, b = [*map(int,input().split())]
        bin_list = []
        if a == 0 and b == 0:
            res = [1]*n
            result = binatodeci(res)
            print(result)
            continue
        elif a == 0 or b == 0:
            tempmax = max(a,b)
            bin_listnum = [int(i) for i in list('{:032b}'.format(tempmax))]
            bin_listnum = bin_listnum[-n:]
            res = [1]*n
            i = 0
            while i < n-1 and bin_listnum[i] == 1 :
                if res[i] == bin_listnum[i]:
                    res[i] = 0
                i += 1
            res[i-1] = 1
            print(binatodeci(res))

        else:


            bin_list.append([int(i) for i in list('{:032b}'.format(a))])
            bin_list.append([int(i) for i in list('{:032b}'.format(b))])
            binA = bin_list[0][-n:]
            binB = bin_list[1][-n:]
            res = [1]*n
            for i in range(n):
                if binA[i] == binB[i] and binA[i] == 1:
                    res[i] = 0
                else:
                    res[i] = 1
            
            result = binatodeci(res)
            # tempres = [1]*n
            # tempresult = binatodeci(tempres)
            # if result == tempresult:
            #     res[0] = 0
            #     result = binatodeci(res)
            while result == a or result == b:
                for i in range(n-1,-1,-1):
                    if res[i] == 1:
                        res[i] = 0
                        break
                result = binatodeci(res)
            print(result)

            # bin_list.append([int(i) for i in list('{:032b}'.format(test_num))])
        
solve()