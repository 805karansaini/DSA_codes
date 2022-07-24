# https://www.codechef.com/JULY222D/problems/BURGERS2
def solve():
    t = int(input())
    while t:
        t-=1
        normal,special,req,money =  [*map(int,input().split())]
        if req*normal > money:
            print(-1)
        elif (req*normal) == money:
            print(req, 0)
        elif special*req <= money:
            print(0,req)
        else:
            # x + y = req
            # normal*x + special*y <= money
            # normal*x + normal*y <= normal*req
            # solve for y.
            # (special-normal)*y <= money - (req*normal)
            # we know special, normal, money, req.. we can find yield
            # now  x = req - y... print(x,y)
            diff = int(special - normal)
            reqNor = req*normal
            y = int((money-reqNor)/diff)
            print(req-y,y)
solve()