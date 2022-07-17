def solve():
    t = int(input())
    while t:
        t-=1
        n, size = [*map(int,input().split())]
        nums = [*map(int,input().split())]

        bin_list = []
        for test_num in nums:
            bin_list.append([ int(i) for i in list('{:%b}'.format(test_num,%size)) ])
        print(bin_list)
        

solve()