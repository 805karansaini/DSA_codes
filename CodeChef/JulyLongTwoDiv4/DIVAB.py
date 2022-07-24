# https://www.codechef.com/JULY222D/problems/DIVAB
def solve():
    t = int(input())
    while t:
        t-=1
        x,y,num =  [*map(int,input().split())]
        if x%y == 0:
            print(-1)
            continue
        mul = (num//x)
        flag = True
        while flag:
            test = mul*x
            if test >= num and test%y != 0:
                flag = False
                print(test)
                break
            mul += 1
solve()# cook your dish here
