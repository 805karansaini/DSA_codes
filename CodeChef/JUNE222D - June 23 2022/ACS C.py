# A is complementary to T.
# T is complementary to A.
# C is complementary to G.
# G is complementary to C.
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        
        if n < 11:
            print(n)
        elif n%100 < 100 and n%100 > 10:
            print("-1")
        else:
            res = 0
            temp = n
            while temp > 99:
                temp = temp-100
                res+=1
                
            res += temp

            if res < 11:
                print(res)
            else:
                print("-1")
         
solve()