def solve():
    t = int(input())

    
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        odd = even = 0
        for nu in nums:
            if nu%2==0:
                even+=1
            else:
                odd+= 1
        print(odd, even, " : first check")
        if odd%2==0 and even%2 == 0:
            print("YES")
            continue
        print(nums)
        temp = []
        i = 0
        while i < n:
            if i+1 < n and (nums[i+1] - nums[i]) == 1:
                i += 1
            else:
                temp.append(nums[i])
            i+=1
        odd = even = 0
        print(temp)

        if len(temp):
            for number in temp:
                if number%2==0:
                    even+=1
                else:
                    odd+= 1
        print(odd, " : odd & even : ", even)
        if odd%2==0 and even%2 == 0:
            print("YES")
        else:
            print("NO")

solve()