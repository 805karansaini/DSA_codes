from collections import defaultdict
import math
def solve():
   
    t = int(input())
    while t:
        t-=1
        num = int(input())
        
        if num%2 == 1:
            print("0")
        else:
            count=0
            a=[]
            rnum = int(math.sqrt(num))
            for num1 in range (1, rnum+1):
                o_sq = num - (num1*num1)
                num2 = int(math.sqrt(o_sq))
                if num2*num2==o_sq:
                    a.append([num1,num2])
            
            x = []
            y = []
            for i in a:
                if i not in x:
                    y.append(i)
                    x.append([ i[1], i[0] ])
            for i in y:
                L = min(i[0],i[1])
                M = max(i[0],i[1]) 
                if i[0]==0 or i[1]==0:
                    count+=1
                else:
                    for j in range(1,M):
                        a = j 
                        b = a+L
                        g = math.gcd(a, b)
                        l=(a*b)//g
                        if (g+l)==M:
                            count+=2
            print(count)
solve()
