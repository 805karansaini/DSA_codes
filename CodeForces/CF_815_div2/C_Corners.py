# Wrong Solution
# fails for Two Diagonals zero in 2x2 cells

from collections import defaultdict

def solve():
    t = int(input())
 
    while t:
        t-=1
        R, C = [*map(int, input().split())]
        grid = [ [ 0 for i in range(C) ] for _ in range(R) ]
        count,zero  = 0, []
        # taking string as input and putting them in grid
        for r in range(R):
            temp = input()
            j = 0
            for c in temp:
                grid[r][j] = int(c)
                if c == "1":
                    count  += 1
                else:
                    zero.append((r,j))
                j+=1
        # if count of 1 == 0 printo 0. if count == R*C print (R*C -2)
        if count == 0:
            print("0")
        elif count == (R*C):
            print((R*C)-2)
        # else there are some zero in the matrix 
        else:
            # directions are to check if we can make a L shape that contains all 0's
            #   D1: |     D2:   |         D3: 0--        D4: --0 
            #       0--       --0             |                |
            dirDia = [ [0,1], [-1,0], [0,-1], [-1,0], [0,1], [1,0], [0,-1], [1,0], [1,1], [-1,-1], [1,-1], [-1,1] ]
            temp = 0 # to count maximum Zeros in L shape

            for i,j in zero:  # list contains x-y co-ordiate of Zero 
                p = 0
                for dx, dy in dirDia:
                    if 0 <= i+dx < R  and 0 <= j+dy < C and grid[i+dx][j+dy] == 0:
                        p += 1
                        if p == 1:
                            break
                if p == 1:
                    break  
               
            
            if p == 1:  # there are no Two zero Adjacent so maximum move will be count - 1
                print(count)
            else: 
                print(count-1)

solve()