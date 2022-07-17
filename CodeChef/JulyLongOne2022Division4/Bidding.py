from traceback import print_tb


def solve():
    t = int(input())
    while t:
        t-=1
        Alice, Bob, Charlie = [*map(int,input().split())]
        if Alice > Bob and Alice > Charlie:
            print("Alice")
        elif Bob > Alice and Bob > Charlie:
            print("Bob")
        else:
            print("Charlie")
       

solve()