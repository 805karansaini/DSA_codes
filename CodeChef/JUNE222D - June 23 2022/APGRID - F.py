# from collections import defaultdict
def solve():
    t = int(input())
    while t:
        t-=1
        row, col = [*map(int,input().split())]
        
        if row<=col:
            matrix= [ [ 1+i for i in range(col) ] for _ in range(row) ]
            for i in range(1,row):
                for j in range(col):
                    matrix[i][j] = matrix[i-1][j] + j+row+1
            
            for x in range(row):
                print(*matrix[x])
        else:
            matrix= [ [ 1 +(col+1)*i for i in range(col) ] for _ in range(row) ]
            for i in range(1,row):
                for j in range(col):
                    matrix[i][j] = matrix[i-1][j] + j+1
            
            for x in range(row):
                print(*matrix[x])

solve()