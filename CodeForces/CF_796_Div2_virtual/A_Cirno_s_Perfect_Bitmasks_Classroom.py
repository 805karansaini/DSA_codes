def solve():
    t = int(input())

    while t:
        t-=1
        n = int(input())
        for i in range(10000000):
            if n & i > 0 and n ^ i > 0:
                print(i)
                break
        # print(c)
    return

solve()