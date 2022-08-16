from collections import defaultdict

def solve():
    t = int(input())
 
    while t:
        t-=1
        n,k = [*map(int, input().split())]
        
        if n < 3:
            if ((1+k)*2) %4==0:
                print("YES")
                print("1 2")
            elif ((2+k)*1) %4==0:
                print("YES")
                print("2 1")
            else:
                print("NO")
            continue
        flag = True
        if n  > 2:
            if flag and ((1+k)*2) %4==0: #1,2 -> 3,4 4,3
                if flag and ((3+k)*4) %4==0:
                    ans1 = [1,2]
                    ans2 = [3,4]
                    flag = False
                    
                if flag and ((4+k)*3) %4==0:
                    ans1 = [1,2]
                    ans2 = [4,3]
                    flag = False

            if flag and ((2+k)*1) %4==0: #2,1 -> 3,4 4,3
                if flag and ((3+k)*4) %4==0:
                    ans1 = [2,1]
                    ans2 = [3,4]
                    flag = False
                    # ANS
                if flag and ((4+k)*3) %4==0:
                    ans1 = [2,1]
                    ans2 = [4,3]
                    flag = False
            
            if flag and ((3+k)*4) %4==0: #3,4-> 1,2 2,1
                if flag and ((1+k)*2) %4==0:
                    ans1 = [3,4]
                    ans2 = [1,2]
                    flag = False
                    # ANS
                if flag and ((2+k)*1) %4==0:
                    ans1 = [3,4]
                    ans2 = [2,1]
                    flag = False
            
            if flag and ((4+k)*3) %4==0: #4,3 -> 1,2 2,1
                if flag and ((1+k)*2) %4==0:
                    ans1 = [4,3]
                    ans2 = [1,2]
                    flag = False
                    # ANS
                if flag and ((2+k)*1) %4==0:
                    ans1 = [4,3]
                    ans2 = [2,1]
                    flag = False
            
        if flag:
            print("NO")
        else:
            print("YES")
            
            i = ans1[0]
            j = ans1[1]
            while i <= n and j <= n:
                print(i, j)
                i+=4
                j+=4
            
            i = ans2[0]
            j = ans2[1]
            while i <= n and j <= n:
                print(i, j)
                i+=4
                j+=4

solve()