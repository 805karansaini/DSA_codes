from collections import defaultdict, Counter
def solve():
    t = int(input())
    while t:
        seen = {}
        t-=1
        N = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        countzero = Counter(nums)
        if countzero[0] == N:
            print("YES")
            continue
        pos = []
        neg = []
        zero = False
        for n in nums:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)
            elif n == 0:
                zero = True
        
        if len(pos) > 2 or len(neg) > 2:
            print("NO")
            continue
        else:
            sett = set(nums)
            templist = pos[:]
            templist = templist + neg[:]
            if zero:
                templist.append(0)
            breakk = False
            # print(templist)
            for i in range(len(templist)):
                for j in range(i+1,len(templist)):
                    for k in range(j+1,len(templist)):
                        if templist[i] + templist[j] + templist[k] not in sett:
                            print("NO")
                            breakk = True
                            break
                    if breakk:
                        break
                if breakk:
                    break
            
            if breakk:
                pass
            else:
                print("YES")
            

solve()