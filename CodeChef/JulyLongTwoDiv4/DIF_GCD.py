# https://www.codechef.com/JULY222D/problems/DIF_GCD

def solve():
    t = int(input())
    while t:
        t-=1
        N,M =  [*map(int,input().split())]
        high = -1
        num1, num2 = None, None
        for i in range(N, min((N*2)+1,M+1)):
            temp = M//i
            if high <= ((temp*i) - i):
                num1, num2 = temp*i, i
                high = ((temp*i) - i)
        print(num1, num2)
solve()# cook your dish here
