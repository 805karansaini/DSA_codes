from typing import Counter


def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        bin = [0]
        
        var = nums[1:]
        var.append(nums[0])
        for b in var:
            if b==0:
                if bin[-1] == 0:
                    bin.append(0)
                else:
                    bin.append(1)
            else:
                if bin[-1] == 0:
                    bin.append(1)
                else:
                    bin.append(0)
        # print(bin)
        if bin[0] == bin[-1]:
            print("YES")
        else:
            print("NO")

solve()